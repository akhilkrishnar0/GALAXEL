from galaxy_flux_pipeline.decals import build_decals_cutout_url

def test_decals_url():
    url = build_decals_cutout_url(10.0, -2.0, 256, 'ls-dr10', 0.262)
    assert 'ra=10.0' in url and 'layer=ls-dr10' in url and 'size=256' in url
