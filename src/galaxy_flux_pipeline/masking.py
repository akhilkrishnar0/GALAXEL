import numpy as np
from photutils.segmentation import detect_threshold, detect_sources, SourceCatalog

def build_mask(image, galaxy_center_xy, protect_radius_pix=20, nsigma=2.5):
    threshold=detect_threshold(image, nsigma=nsigma)
    segm=detect_sources(image, threshold, npixels=10)
    if segm is None: return np.zeros_like(image,dtype=bool), None
    cat=SourceCatalog(image, segm)
    mask=np.zeros_like(image,dtype=bool)
    yy,xx=np.indices(image.shape)
    for src in cat:
        compact=(src.eccentricity<0.8) and (src.area.value<300)
        d=((src.xcentroid-galaxy_center_xy[0])**2 + (src.ycentroid-galaxy_center_xy[1])**2)**0.5
        if compact and d>protect_radius_pix:
            mask |= segm.data==src.label
    return mask, cat
