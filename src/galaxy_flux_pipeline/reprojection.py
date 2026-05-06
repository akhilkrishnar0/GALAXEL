from __future__ import annotations
import numpy as np
from reproject import reproject_exact

def reproject_to(data, src_wcs, out_wcs, shape_out):
    return reproject_exact((data, src_wcs), out_wcs, shape_out=shape_out)

def integrated_flux(arr: np.ndarray) -> float:
    return float(np.nansum(arr))
