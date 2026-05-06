import numpy as np
from galaxy_flux_pipeline.cropping import center_crop

def test_crop_shape():
    x=np.zeros((10,10))
    assert center_crop(x,4).shape==(4,4)
