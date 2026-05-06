from __future__ import annotations
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from reproject import reproject_interp


def exposure_weighted_stack(images: list[np.ndarray], exposures: list[np.ndarray]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    cube = np.stack(images)
    ecube = np.stack(exposures)
    valid = np.isfinite(cube) & np.isfinite(ecube) & (ecube > 0)
    weighted_sum = np.nansum(np.where(valid, cube * ecube, 0.0), axis=0)
    exp_sum = np.nansum(np.where(valid, ecube, 0.0), axis=0)
    out = np.divide(weighted_sum, exp_sum, out=np.full_like(weighted_sum, np.nan), where=exp_sum > 0)
    err = np.divide(1.0, np.sqrt(exp_sum), out=np.full_like(exp_sum, np.nan), where=exp_sum > 0)
    return out, exp_sum, err


def stack_galex_fits(science_paths: list[Path], exposure_paths: list[Path], out_science: Path, out_exposure: Path, out_err: Path) -> None:
    if not science_paths or len(science_paths) != len(exposure_paths):
        raise ValueError("science/exposure path lists must be non-empty and same length")
    ref_hdu = fits.open(science_paths[0])[0]
    ref_wcs = WCS(ref_hdu.header)
    shape = ref_hdu.data.shape
    images, exps = [], []
    for sp, ep in zip(science_paths, exposure_paths):
        sd, sh = fits.getdata(sp, header=True)
        ed, eh = fits.getdata(ep, header=True)
        ri, _ = reproject_interp((sd, WCS(sh)), ref_wcs, shape_out=shape)
        re, _ = reproject_interp((ed, WCS(eh)), ref_wcs, shape_out=shape)
        images.append(ri)
        exps.append(re)
    sci, exp, err = exposure_weighted_stack(images, exps)
    h = ref_hdu.header.copy(); h["BUNIT"] = "count/s"; h["HIERARCH STACK"] = "exposure_weighted"
    fits.writeto(out_science, sci.astype("f4"), h, overwrite=True)
    he = h.copy(); he["BUNIT"] = "s"
    fits.writeto(out_exposure, exp.astype("f4"), he, overwrite=True)
    herr = h.copy(); herr["BUNIT"] = "(count/s)"
    fits.writeto(out_err, err.astype("f4"), herr, overwrite=True)
