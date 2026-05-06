from __future__ import annotations
import numpy as np
import pandas as pd

def square_grid(shape: tuple[int,int], cell_px: int) -> pd.DataFrame:
    rows=[]; idx=0
    ny,nx=shape
    for y in range(0,ny,cell_px):
        for x in range(0,nx,cell_px):
            rows.append({"id":idx,"x":x,"y":y,"x1":min(x+cell_px,nx),"y1":min(y+cell_px,ny)}); idx+=1
    return pd.DataFrame(rows)
