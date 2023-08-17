from pathlib import Path

import pandas as pd
from PIL import Image

if __name__ == "__main__":

    DATA_DIR = Path("MissingDataOpenData")

    SPLIT_DIR = DATA_DIR / "data_splits"
    SAVE_DIR = DATA_DIR / ("split_dirs")
    SAVE_DIR.mkdir(parents=True, exist_ok=True)
    
    MASKED_DIR = DATA_DIR / "masked"
    MASKS_DIR = DATA_DIR / "masks"

    for split_file_name in SPLIT_DIR.glob("*.txt"):
        split_name = split_file_name.stem
        if split_name == "training":
            continue
        split_folder = SAVE_DIR / split_name
        split_folder.mkdir(parents=True, exist_ok=True)

        file_ids = split_file_name.open("r").readlines()
        file_ids = [file_id.strip() for file_id in file_ids]

        for id in file_ids:
            masked_image = Image.open(MASKED_DIR / (id + "_stroke_masked.png"))
            mask = Image.open(MASKS_DIR / (id + "_stroke_mask.png"))
            
            masked_image.save(split_folder / (id + ".png"))
            mask.save(split_folder / (id + "_mask.png"))


    