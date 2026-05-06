import numpy as np

def compare_flux(before,after):
    frac=(after-before)/np.where(before!=0,before,np.nan)
    return {'mean':float(np.nanmean(frac)), 'median':float(np.nanmedian(frac)), 'std':float(np.nanstd(frac))}
