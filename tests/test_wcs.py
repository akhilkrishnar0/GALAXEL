from galaxy_flux_pipeline.wcs_utils import make_simple_wcs

def test_wcs_roundtrip():
    w=make_simple_wcs()
    ra,dec=w.pixel_to_world_values(50,50)
    assert isinstance(ra,float)
