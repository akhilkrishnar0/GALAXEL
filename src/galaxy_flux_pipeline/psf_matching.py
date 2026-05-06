from __future__ import annotations
import numpy as np
from astropy.convolution import Gaussian2DKernel, convolve_fft

def match_psf(image: np.ndarray, current_fwhm: float, target_fwhm: float, pixscale: float) -> np.ndarray:
    if target_fwhm <= current_fwhm:
        return image
    sigma=np.sqrt(target_fwhm**2-current_fwhm**2)/2.3548/pixscale
    k=Gaussian2DKernel(sigma)
    return convolve_fft(image,k,boundary='fill',fill_value=0.0,normalize_kernel=True)
