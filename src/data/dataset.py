from pathlib import Path
from typing import Callable, Optional

import pandas as pd
from PIL import Image
from torch.utils.data import Dataset


class RetinopathyDataset(Dataset):
    """Dataset wrapper for retinal fundus images and binary DR labels."""

    def __init__(
        self,
        csv_path: str,
        image_dir: str,
        transform: Optional[Callable] = None,
        image_col: str = "image",
        label_col: str = "label",
    ):
        self.df = pd.read_csv(csv_path)
        self.image_dir = Path(image_dir)
        self.transform = transform
        self.image_col = image_col
        self.label_col = label_col

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        image_path = self.image_dir / row[self.image_col]
        image = Image.open(image_path).convert("RGB")
        label = int(row[self.label_col])

        if self.transform:
            image = self.transform(image)

        return image, label
