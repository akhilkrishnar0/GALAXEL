import numpy as np
from galaxy_flux_pipeline.stacking import exposure_weighted_stack

def test_stack():
    s,e,er=exposure_weighted_stack([np.ones((2,2)),2*np.ones((2,2))],[np.ones((2,2)),np.ones((2,2))])
    assert np.allclose(s,1.5)
