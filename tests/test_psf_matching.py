import numpy as np
from galaxy_flux_pipeline.psf_matching import match_psf

def test_psf_match_preserves_shape():
    img=np.random.random((20,20))
    out=match_psf(img,1.0,5.3,0.25)
    assert out.shape==img.shape
