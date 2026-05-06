from __future__ import annotations
import numpy as np
from scipy import ndimage
from photutils.segmentation import detect_threshold, detect_sources, SourceCatalog


def build_mask(image: np.ndarray, nsigma: float = 2.0, npixels: int = 8, protect_center_px: float = 30.0, compactness_max: float = 0.55, dilate_pixels: int = 2) -> tuple[np.ndarray, np.ndarray]:
    thr = detect_threshold(image, nsigma=nsigma)
    seg = detect_sources(image, thr, npixels=npixels)
    if seg is None:
        z = np.zeros_like(image, dtype=bool)
        return z, z
    cat = SourceCatalog(image, seg)
    yy, xx = np.indices(image.shape)
    cy, cx = np.array(image.shape) / 2.0
    r = np.hypot(xx - cx, yy - cy)
    protect = r <= protect_center_px
    mask = np.zeros_like(image, dtype=bool)
    for src in cat:
        lab = src.label
        area = float(src.segment_area.value)
        ecc = float(src.eccentricity.value) if hasattr(src.eccentricity, "value") else float(src.eccentricity)
        eqr = np.sqrt(area / np.pi)
        comp = eqr / max(src.semimajor_sigma.value if hasattr(src.semimajor_sigma, "value") else float(src.semimajor_sigma), 1e-6)
        candidate = (comp <= compactness_max) and (ecc < 0.95)
        srcmask = seg.data == lab
        if np.any(srcmask & protect):
            continue
        if candidate:
            mask |= srcmask
    if dilate_pixels > 0:
        mask = ndimage.binary_dilation(mask, iterations=dilate_pixels)
    return mask, seg.data > 0
