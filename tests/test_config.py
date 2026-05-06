from galaxy_flux_pipeline.config import load_config

def test_load_config():
    cfg=load_config('configs/default.yaml')
    assert cfg.grid_cell_size_arcsec==6.0
