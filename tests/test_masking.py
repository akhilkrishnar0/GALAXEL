import numpy as np
from galaxy_flux_pipeline.masking import build_mask

def test_masking_runs():
    img=np.random.normal(0,1,(64,64)); img[5:8,5:8]+=15
    m,_=build_mask(img,(32,32))
    assert m.shape==img.shape
