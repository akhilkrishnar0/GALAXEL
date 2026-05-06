from __future__ import annotations
import numpy as np
import pandas as pd

NANOMAGGY_TO_MJY = 3.631e-3
GALEX_AB_ZP = {"FUV": 18.82, "NUV": 20.08}


def cps_to_mjy(cps: np.ndarray, band: str) -> np.ndarray:
    zp = GALEX_AB_ZP[band]
    mag = -2.5 * np.log10(np.clip(cps, 1e-30, None)) + zp
    return 10 ** ((16.4 - mag) / 2.5)


def nanomaggy_to_mjy(val: np.ndarray) -> np.ndarray:
    return val * NANOMAGGY_TO_MJY


def measure_grid_flux(table: pd.DataFrame, band_images: dict[str, np.ndarray], band_errs: dict[str, np.ndarray], master_mask: np.ndarray | None = None, max_mask_frac: float = 0.5) -> pd.DataFrame:
    out = table.copy()
    flags = []
    for i, r in table.iterrows():
        sl = (slice(int(r.y), int(r.y1)), slice(int(r.x), int(r.x1)))
        mfrac = float(np.mean(master_mask[sl])) if master_mask is not None else 0.0
        flags.append(1 if mfrac > max_mask_frac else 0)
    out["flag_bad"] = flags
    for b, img in band_images.items():
        flux, err = [], []
        for _, r in table.iterrows():
            sl = (slice(int(r.y), int(r.y1)), slice(int(r.x), int(r.x1)))
            arr = img[sl].copy()
            if master_mask is not None:
                arr = np.where(master_mask[sl], np.nan, arr)
            flux.append(np.nansum(arr))
            earr = band_errs[b][sl]
            err.append(float(np.sqrt(np.nansum(np.where(np.isfinite(arr), earr**2, 0.0)))))
        out[b] = flux; out[f"{b}_err"] = err
    return out
