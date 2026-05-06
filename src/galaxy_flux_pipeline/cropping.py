from __future__ import annotations
import numpy as np

def center_crop(image: np.ndarray, size_px: int) -> np.ndarray:
    y,x=image.shape
    cy,cx=y//2,x//2
    h=size_px//2
    return image[cy-h:cy+h,cx-h:cx+h]
