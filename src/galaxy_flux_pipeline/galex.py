from __future__ import annotations
from pathlib import Path
from typing import Iterable
import json
from astroquery.mast import Observations
from astropy.table import Table

GALEX_KEYWORDS = ("int", "cnt", "exp", "rrhr", "skybg", "bg", "sigma", "wt")


def query_galex_products(ra: float, dec: float, radius_deg: float) -> tuple[Table, Table]:
    obs = Observations.query_region(f"{ra} {dec}", radius=f"{radius_deg} deg", obs_collection="GALEX")
    products = Observations.get_product_list(obs) if len(obs) else Table()
    return obs, products


def select_science_products(products: Table) -> Table:
    if len(products) == 0:
        return products
    names = [str(x).lower() for x in products["productFilename"]]
    mask = [any(k in n for k in GALEX_KEYWORDS) and n.endswith(("fits", "fits.gz")) for n in names]
    return products[mask]


def group_products_by_band(products: Table) -> dict[str, list[dict]]:
    out = {"FUV": [], "NUV": []}
    for row in products:
        fname = str(row["productFilename"]).lower()
        band = "FUV" if "fd" in fname or "fuv" in fname else "NUV" if "nd" in fname or "nuv" in fname else None
        if band:
            out[band].append({k: (row[k].item() if hasattr(row[k], "item") else row[k]) for k in row.colnames})
    return out


def write_product_bookkeeping(path: Path, obs: Table, selected: Table) -> None:
    payload = {
        "n_observations": int(len(obs)),
        "n_selected_products": int(len(selected)),
        "selected_filenames": [str(x) for x in selected["productFilename"]] if len(selected) else [],
    }
    path.write_text(json.dumps(payload, indent=2))
