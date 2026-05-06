import numpy as np
from galaxy_flux_pipeline.psf_matching import match_psf, propagate_error_convolution

def test_psf_flux_nearly_conserved():
    x=np.zeros((51,51)); x[25,25]=1.0
    y=match_psf(x,1.5,5.3,1.0)
    assert abs(np.nansum(y)-1.0)<1e-3

def test_error_propagation_positive():
    e=np.ones((21,21))*0.1
    out=propagate_error_convolution(e,2.0,5.3,1.0)
    assert np.nanmedian(out)>0
