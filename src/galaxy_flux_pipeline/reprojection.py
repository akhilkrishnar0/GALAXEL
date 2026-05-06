from __future__ import annotations
from reproject import reproject_interp

def reproject_to(data, src_wcs, out_wcs, shape_out):
    return reproject_interp((data, src_wcs), out_wcs, shape_out=shape_out)
