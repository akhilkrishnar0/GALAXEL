from __future__ import annotations
import numpy as np
import pandas as pd
from astropy.wcs import WCS

def square_grid(shape: tuple[int, int], cell_px: int, wcs: WCS | None = None) -> pd.DataFrame:
    rows = []; idx = 0
    ny, nx = shape
    for y0 in range(0, ny, cell_px):
        for x0 in range(0, nx, cell_px):
            y1, x1 = min(y0 + cell_px, ny), min(x0 + cell_px, nx)
            cx, cy = (x0 + x1 - 1) / 2, (y0 + y1 - 1) / 2
            row = {"id": idx, "x": x0, "y": y0, "x1": x1, "y1": y1}
            if wcs is not None:
                ra, dec = wcs.pixel_to_world_values(cx, cy)
                row["ra"] = float(ra); row["dec"] = float(dec)
            rows.append(row); idx += 1
    return pd.DataFrame(rows)
