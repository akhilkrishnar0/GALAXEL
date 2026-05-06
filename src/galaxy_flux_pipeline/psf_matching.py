import numpy as np
from scipy.ndimage import gaussian_filter

def match_psf(image,current_fwhm,target_fwhm,pixscale):
    if target_fwhm<=current_fwhm: return image.copy()
    sig=lambda f: f/(2.3548*pixscale)
    kernel=(sig(target_fwhm)**2-sig(current_fwhm)**2)**0.5
    return gaussian_filter(image,kernel,mode='nearest')
