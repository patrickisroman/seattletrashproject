# Seattle Trash Project

<center>
<img src="https://s3.us-west-2.amazonaws.com/seattletrashproject.com/1.png" width="200" height="200">
<img src="https://s3.us-west-2.amazonaws.com/seattletrashproject.com/2.png" width="300" height="200">
<img src="https://s3.us-west-2.amazonaws.com/seattletrashproject.com/3.png" width="300" height="200">
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

Each annotation in the dataset contains four keys:
- element: the type of object | ex: `beverage bottle, cigarette, bottlecap, etc.`
- material: the material the object is made of | ex: `polyethylene terephthalate, polypropylene, aluminum, etc.`
- mass: the mass of the object in grams (g) | ex: `15`
- quality: rough probability an item can be repurposed [0-1.0] | ex: `0.59`

The coco category map defaults to element. `annotations` will include a categoryMap which maps keys to category id, ex: 
```
categoryMap = {
    "beverage bottle" : 1,
    "bottlecap" : 2,
    ...
}
```