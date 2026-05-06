from __future__ import annotations
import numpy as np
from astropy.convolution import Gaussian2DKernel, convolve_fft


def match_psf(image: np.ndarray, current_fwhm: float, target_fwhm: float, pixscale: float) -> np.ndarray:
    if target_fwhm <= current_fwhm:
        return image.copy()
    sigma_pix = np.sqrt(target_fwhm**2 - current_fwhm**2) / 2.354820045 / pixscale
    kernel = Gaussian2DKernel(sigma_pix)
    out = convolve_fft(image, kernel, boundary="fill", fill_value=0.0, normalize_kernel=True, allow_huge=True)
    return out


def propagate_error_convolution(err_image: np.ndarray, current_fwhm: float, target_fwhm: float, pixscale: float) -> np.ndarray:
    if target_fwhm <= current_fwhm:
        return err_image.copy()
    sigma_pix = np.sqrt(target_fwhm**2 - current_fwhm**2) / 2.354820045 / pixscale
    kernel = Gaussian2DKernel(sigma_pix).array
    var = err_image**2
    var_conv = convolve_fft(var, kernel**2, boundary="fill", fill_value=0.0, normalize_kernel=False, allow_huge=True)
    return np.sqrt(np.clip(var_conv, 0, None))
