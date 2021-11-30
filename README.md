# Seattle Trash Project

<center >
<img src="https://s3.us-west-2.amazonaws.com/seattletrashproject.com/4.png">
</center>

---

To view the dataset, visit https://seattletrashproject.com

**Seattle Trash Project** (STP) is an open-source vision dataset of post-consumer waste identified in Seattle. The dataset is hosted in S3/Dynamo (AWS) and is available for public scaled consumption.

**Note:** Please be courteous when downloading data from the dataset. The dataset is provided publicly at no cost but hosting and accessing the dataset is not free. Transfers are collectively throttled so downloading multiple times might block someone else from downloading the dataset.

# Download

First, install dependencies:

```
# pip install boto3 requests
```

To download the raw dataset, run:

```
# python download_stp.py
```

This will download `annotations.json` containing a coco-compatible dataset file. This will also download the raw images (.png) from the dataset into the `./images` subdirectory. As of 11/2021 the raw dataset is ~4.86GB.

To download the downsized dataset, run:
```
# python download_stp.py --small
```

This will download `annotations.json` containing a coco-comaptible dataset file. This will also download the miniaturized image (.png) for each element from the dataset into the `./images-small` subdirectory. As of 11/2021, the small dataset is ~424MB.

# Format

Example annotation:
```
{
    "id": 225,
    "file_name": "images/0634df25e6cde74c3de7283ae109f6f6.png",
    "s3key": "images/0634df25e6cde74c3de7283ae109f6f6.png",
    "small_file_name": "images-small/0634df25e6cde74c3de7283ae109f6f6.png",
    "small_s3key": "images-small/0634df25e6cde74c3de7283ae109f6f6.png",
    "height": 4032,
    "width": 3024,
    "material": "low-density polyethylene",
    "element": "resealable food bag",
    "mass": 2.0,
    "quality": 0.75,
    "producer": null
}
```

Each annotation in the dataset contains four keys:
- **element**: the type of object | ex: `beverage bottle, cigarette, bottlecap, etc.`
- **material**: the dominant material the object is made of | ex: `polypropylene, aluminum, etc.`
- **mass**: the mass of the object in grams (g) | ex: `15`
- **quality**: rough probability a post-consumer item can be recovered [0-1.0] | ex: `0.59`

The `producer` key is optional, and indicates which producer is associated with the item. The coco category map defaults to `element`. `annotations.json` will include a `categoryMap` object which maps keys to category id, ex: 

```
categoryMap = {
    "beverage bottle" : 1,
    "bottlecap" : 2,
    ...
}
```
