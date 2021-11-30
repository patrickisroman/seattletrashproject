import boto3
import json
import multiprocessing
import requests
import argparse

from decimal import Decimal
from pathlib import Path

BUCKET_NAME = 'recyclr-dataset'
IMAGE_PATH = 'images/'
SMALL_IMAGE_PATH = 'images-small/'

config_map = {
    'small' : {
        'path': 'images-small/',
        'key': 'small_file_name'
    },
    'regular' : {
        'path': 'images/',
        'key': 'file_name'
    }
}

# Parse arguments
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--small", action="store_true")
args = parser.parse_args()

# Create client
s3 = boto3.client('s3', region_name='us-west-2')
mode = "small" if args.small else "regular"

def download_image(image):
    s3.download_file(BUCKET_NAME, image[config_map[mode]['key']], image[config_map[mode]['key']])

def get_coco_dataset():
    dataset = json.loads(requests.get('https://prw168zo7a.execute-api.us-west-2.amazonaws.com/prod/coco').content)
    
    path = Path(config_map[mode]['path'])
    if not path.exists():
        path.mkdir()

    print('Downloading images to', path.absolute())
    pool = multiprocessing.Pool(10)
    pool.map(download_image, dataset['images'])
    pool.close()
    pool.join()

    print('Writing annotations')
    with open('annotations.json', 'w+') as fd:
        fd.write(json.dumps(dataset, indent=4))

# run
get_coco_dataset()