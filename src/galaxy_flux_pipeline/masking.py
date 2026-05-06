from __future__ import annotations
import numpy as np
from photutils.segmentation import detect_threshold, detect_sources

def build_mask(image: np.ndarray, nsigma: float=2.5, npixels: int=8, protect_center_px: float=30.0) -> np.ndarray:
    thr=detect_threshold(image, nsigma=nsigma)
    seg=detect_sources(image, thr, npixels=npixels)
    if seg is None:
        return np.zeros_like(image,dtype=bool)
    mask=seg.data>0
    yy,xx=np.indices(image.shape)
    cy,cx=np.array(image.shape)//2
    protect=((xx-cx)**2+(yy-cy)**2)<=protect_center_px**2
    mask[protect]=False
    return mask
