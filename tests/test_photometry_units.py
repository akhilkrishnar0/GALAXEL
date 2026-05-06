import numpy as np
from galaxy_flux_pipeline.photometry import cps_to_mjy

def test_cps_to_mjy_positive():
    assert np.all(cps_to_mjy(np.array([1.0]),18.82)>0)
