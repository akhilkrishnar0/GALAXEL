from dataclasses import dataclass, field
from pathlib import Path
import json, yaml

@dataclass
class PipelineConfig:
    crop_size_arcsec: float = 240.0
    decals_layer: str = "ls-dr10"
    decals_pixscale: float = 0.25
    galex_search_radius: float = 0.2
    target_psf_fwhm_arcsec: float = 5.3
    grid_cell_size_arcsec: float = 6.0
    masking_threshold_sigma: float = 2.5
    galaxy_protection_radius_arcsec: float = 20.0
    random_aperture_count: int = 200
    output_units: str = "mJy"
    logging_level: str = "INFO"
    overwrite: bool = False

def load_config(path:str|Path)->PipelineConfig:
    p=Path(path)
    raw=json.loads(p.read_text()) if p.suffix=='.json' else yaml.safe_load(p.read_text())
    return PipelineConfig(**(raw or {}))
