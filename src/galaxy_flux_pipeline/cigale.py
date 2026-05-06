from __future__ import annotations
import pandas as pd

def export_cigale(df: pd.DataFrame, redshift: float=0.0) -> pd.DataFrame:
    out=pd.DataFrame({"id":df["id"],"redshift":redshift,
    "galex.FUV":df["FUV"],"galex.FUV_err":df["FUV_err"],"galex.NUV":df["NUV"],"galex.NUV_err":df["NUV_err"],
    "decals.g":df["g"],"decals.g_err":df["g_err"],"decals.r":df["r"],"decals.r_err":df["r_err"],"decals.z":df["z"],"decals.z_err":df["z_err"]})
    return out
