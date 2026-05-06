from __future__ import annotations
import numpy as np

def flux_stats(before: np.ndarray, after: np.ndarray) -> dict:
    frac=(after-before)/np.where(before==0,np.nan,before)
    return {"mean":float(np.nanmean(frac)),"median":float(np.nanmedian(frac)),"std":float(np.nanstd(frac))}
