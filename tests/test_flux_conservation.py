import numpy as np
from galaxy_flux_pipeline.validation import compare_flux

def test_compare_flux():
    b=np.array([1,2,3.0]); a=np.array([1.01,2.0,3.02])
    s=compare_flux(b,a)
    assert abs(s['mean'])<0.05
