from __future__ import annotations
from pathlib import Path
from urllib.parse import urlencode
import requests

BASE_URL = "https://www.legacysurvey.org/viewer/cutout.fits"


def build_decals_cutout_url(ra: float, dec: float, size: int, layer: str, pix: float) -> str:
    q = urlencode({"ra": ra, "dec": dec, "pix": pix, "layer": layer, "size": size})
    return f"{BASE_URL}?{q}"


def download_decals_cutout(ra: float, dec: float, size: int, layer: str, pix: float, out: Path) -> Path:
    url = build_decals_cutout_url(ra=ra, dec=dec, size=size, layer=layer, pix=pix)
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(r.content)
    return out
