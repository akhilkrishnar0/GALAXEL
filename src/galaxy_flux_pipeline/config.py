from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
import json
import yaml

@dataclass
class PipelineConfig:
    output_root: str = "outputs"
    crop_size_arcsec: float = 240.0
    decals_layer: str = "ls-dr10"
    decals_pixscale: float = 0.25
    galex_search_radius: float = 0.2
    target_psf_fwhm_arcsec: float = 5.3
    grid_cell_size_arcsec: float = 6.0
    random_aperture_count: int = 200
    logging_level: str = "INFO"
    overwrite: bool = False
    masking: dict = field(default_factory=lambda: {"nsigma": 2.5, "npixels": 8, "protect_radius_arcsec": 45.0})


def load_config(path: str | Path) -> PipelineConfig:
    p = Path(path)
    data = json.loads(p.read_text()) if p.suffix.lower()==".json" else yaml.safe_load(p.read_text())
    return PipelineConfig(**(data or {}))
