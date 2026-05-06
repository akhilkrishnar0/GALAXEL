from __future__ import annotations
import numpy as np
import pandas as pd

NANOMAGGY_TO_MJY = 3.631e-3

def cps_to_mjy(cps: np.ndarray, zero_point_ab: float) -> np.ndarray:
    mag = -2.5*np.log10(np.clip(cps,1e-30,None)) + zero_point_ab
    return 10**((16.4-mag)/2.5)

def measure_grid_flux(table: pd.DataFrame, band_images: dict[str,np.ndarray], band_errs: dict[str,np.ndarray]) -> pd.DataFrame:
    out=table.copy()
    for b,img in band_images.items():
        flux=[]; err=[]
        for _,r in table.iterrows():
            sl=(slice(int(r.y),int(r.y1)),slice(int(r.x),int(r.x1)))
            flux.append(np.nansum(img[sl]))
            err.append(np.sqrt(np.nansum(band_errs[b][sl]**2)))
        out[b]=flux; out[f"{b}_err"]=err
    return out
