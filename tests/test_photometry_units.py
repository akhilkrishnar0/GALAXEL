import numpy as np
from galaxy_flux_pipeline.photometry import cps_to_mjy, nanomaggy_to_mjy

def test_cps_to_mjy_positive():
    assert np.all(cps_to_mjy(np.array([1.0]),"FUV")>0)

def test_nanomaggy_to_mjy():
    assert np.isclose(nanomaggy_to_mjy(np.array([1.0]))[0],3.631e-3)
