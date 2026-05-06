import numpy as np
from galaxy_flux_pipeline.psf_matching import match_psf

def test_psf_noop():
    x=np.ones((10,10))
    y=match_psf(x,5.3,5.3,1.0)
    assert np.allclose(x,y)
