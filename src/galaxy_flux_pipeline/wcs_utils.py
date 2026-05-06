from __future__ import annotations
from astropy.wcs import WCS

def pixel_scale_arcsec(wcs: WCS) -> float:
    return abs(wcs.wcs.cdelt[0]) * 3600.0
