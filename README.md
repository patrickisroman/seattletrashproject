# Seattle Trash Project

To view the dataset, visit https://seattletrashproject.com

**Seattle Trash Project** (STP) is an open-source vision dataset of post-consumer waste identified in Seattle. The dataset is hosted in S3/Dynamo (AWS) and is available for public scaled consumption.

**Note:** Please be courteous when downloading data from the dataset. The dataset is provided publicly at no cost but hosting and accessing the dataset is not free. Transfers are collectively throttled so downloading multiple times might block someone else from downloading the dataset.

# Download

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