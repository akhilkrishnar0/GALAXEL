import numpy as np
from galaxy_flux_pipeline.masking import build_mask

def test_mask_runs_and_protects_center():
    y,x=np.indices((100,100))
    galaxy=np.exp(-((x-50)**2+(y-50)**2)/200)
    stars=np.zeros((100,100)); stars[10,10]=15; stars[80,80]=12
    img=galaxy+stars
    mask,_=build_mask(img,protect_center_px=20)
    assert mask[10,10]
    assert not mask[50,50]
