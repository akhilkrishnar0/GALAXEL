from __future__ import annotations
import numpy as np


def center_crop(image: np.ndarray, size_px: int) -> np.ndarray:
    if size_px <= 0:
        raise ValueError("size_px must be positive")
    y, x = image.shape
    size_px = min(size_px, y, x)
    cy, cx = y // 2, x // 2
    h0 = size_px // 2
    h1 = size_px - h0
    return image[cy-h0:cy+h1, cx-h0:cx+h1]
