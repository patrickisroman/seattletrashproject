# Seattle Trash Project

<p align="center">
<img src="https://seattletrashproject.com/img/stp-black.png" style="padding: 10px" width="300">
</p>

<center>
<img src="https://s3.us-west-2.amazonaws.com/seattletrashproject.com/4.png">
</center>

---

To view the dataset, visit https://seattletrashproject.com

**Seattle Trash Project** (STP) is an open-source vision dataset of post-consumer waste identified in Seattle. The dataset is hosted in S3/Dynamo (AWS) and is available for public scaled consumption.

**Note:** Please be courteous when downloading data from the dataset. The dataset is provided publicly at no cost but hosting and accessing the dataset is not free. Transfers are collectively throttled so downloading multiple times might block someone else from downloading the dataset.

# Download

## Manual

The dataset is hosted in S3 & Dynamo. The S3 bucket with dataset images is public and can be accessed via web or with AWS SDKs. Annotations are hosted in Dynamo and can be accessed via API Gateway endpoints.

**S3 Bucket:** `recyclr-dataset`
- Contains image .png files. Each object key is named with the md5 sum of the raw image.

**Coco Dataset Generator:** https://prw168zo7a.execute-api.us-west-2.amazonaws.com/prod/coco
- Creates a coco json file that can be used to train or evaluate models.

## Automated
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
    "segmentation": [
        [
            1769.1874322860226,
            2300.671722643552,
            1463.4019501625125,
            2624.6587215601285,
            1448.8407367280597,
            2608.2773564463687,
            1754.6262188515698,
            2282.470205850486
        ]
    ],
    "bbox": [
        1448.8407367280597,
        2282.470205850486,
        320.3466955579629,
        342.1885157096426
    ],
    "image_id": 0,
    "category_id": 54,
    "id": 0,
    "iscrowd": 0,
    "material": "polypropylene",
    "element": "straw",
    "mass": 2.0,
    "quality": 0.87,
    "producer": "mcdonalds"
}
```

Each annotation in the dataset contains four keys:
| Key  | Description | Example |
| ------------- | ------------- | ---- |
| **material**  | the dominant material the object is made of  | `polypropylene, aluminum, fiber, etc.`|
| **element** | the type (class) of object | `beverage bottle, cigarette, bottlecap, etc.` |
| **mass** | the mass (g) of an object in grams | `15.0`
| **quality** | rough probability a post-consumer item can be recovered [0-1.0] | `0.59`
| **producer** | (optional) producer associated with the item | `coca cola, starbucks, etc.`


The coco category map defaults to `element`. `annotations.json` will include a `categoryMap` object which maps class names to `category_id`, ex: 

```
categoryMap = {
    "beverage bottle" : 1,
    "bottlecap" : 2,
    ...
}
```
