import numpy as np
from galaxy_flux_pipeline.masking import build_mask

def test_mask_runs():
    img=np.random.normal(0,1,(50,50)); img[5,5]=20
    m=build_mask(img)
    assert m.shape==img.shape
