from __future__ import annotations
import numpy as np

def exposure_weighted_stack(images: list[np.ndarray], exposures: list[np.ndarray]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    wsum=np.nansum(np.stack(exposures),axis=0)
    isum=np.nansum(np.stack([i*e for i,e in zip(images,exposures)]),axis=0)
    stacked=np.divide(isum,wsum,out=np.full_like(isum,np.nan),where=wsum>0)
    err=np.divide(1.0,np.sqrt(wsum),out=np.full_like(wsum,np.nan),where=wsum>0)
    return stacked,wsum,err
