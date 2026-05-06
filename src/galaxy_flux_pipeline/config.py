from __future__ import annotations
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any
import json
import yaml


@dataclass
class PipelineConfig:
    output_root: str = "outputs"
    crop_size_arcsec: float = 240.0
    decals_layer: str = "ls-dr10"
    decals_pixscale: float = 0.262
    galex_search_radius: float = 0.25
    target_psf_fwhm_arcsec: float = 5.3
    grid_cell_size_arcsec: float = 6.0
    random_aperture_count: int = 200
    logging_level: str = "INFO"
    overwrite: bool = False
    validate_name_coords: bool = True
    name_coord_tolerance_arcsec: float = 10.0
    masking: dict[str, Any] = field(default_factory=lambda: {
        "nsigma": 2.0,
        "npixels": 8,
        "protect_radius_arcsec": 45.0,
        "compactness_max": 0.55,
        "dilate_pixels": 2,
    })

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def load_config(path: str | Path) -> PipelineConfig:
    p = Path(path)
    raw = p.read_text()
    data = json.loads(raw) if p.suffix.lower() == ".json" else yaml.safe_load(raw)
    return PipelineConfig(**(data or {}))
