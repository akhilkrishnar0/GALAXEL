from __future__ import annotations
from pathlib import Path
import requests
URL_TEMPLATE_FITS = "https://www.legacysurvey.org/viewer/cutout.fits?ra={ra}&dec={dec}&pix={pix}&layer={layer}&size={size}"

def download_decals_cutout(ra: float, dec: float, size: int, layer: str, pix: float, out: Path) -> Path:
    url = URL_TEMPLATE_FITS.format(ra=ra,dec=dec,pix=pix,layer=layer,size=size)
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    out.write_bytes(r.content)
    return out
