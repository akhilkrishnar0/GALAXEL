import numpy as np
from galaxy_flux_pipeline.stacking import exposure_weighted_stack

def test_stack():
    img=np.ones((2,4,4)); exp=np.ones((2,4,4))*2
    out,emap,err=exposure_weighted_stack(img,exp)
    assert np.allclose(out,1)
    assert np.all(emap==4)
