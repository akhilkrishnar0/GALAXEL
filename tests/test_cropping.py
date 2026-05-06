import numpy as np
from galaxy_flux_pipeline.wcs_utils import make_simple_wcs
from galaxy_flux_pipeline.cropping import crop_to_size

def test_crop():
    data=np.zeros((100,100)); w=make_simple_wcs(100,100,ra=10,dec=10)
    c=crop_to_size(data,w,10,10,20)
    assert c.data.size>0
