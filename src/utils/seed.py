import random
import numpy as np
import torch


def set_seed(seed: int = 1337) -> None:
    """Set seeds for reproducible experiments."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
