from astropy.wcs import WCS
from galaxy_flux_pipeline.wcs_utils import pixel_scale_arcsec

def test_pixscale():
    w=WCS(naxis=2); w.wcs.cdelt=[-1/3600,1/3600]
    assert abs(pixel_scale_arcsec(w)-1.0)<1e-6
