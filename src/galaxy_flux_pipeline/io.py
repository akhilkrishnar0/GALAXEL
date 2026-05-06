from __future__ import annotations
from pathlib import Path
import hashlib
import pandas as pd

REQ_COLS = ["galaxy_name", "ra", "dec", "distance_mpc"]

def read_targets(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    for c in REQ_COLS:
        if c not in df.columns:
            raise ValueError(f"Missing required column: {c}")
    return df

def ensure_dirs(base: Path) -> dict[str, Path]:
    dirs = {k: base/k for k in ["raw","intermediate","masks","psfmatched","reproj","photometry","figures","logs","provenance"]}
    for d in dirs.values():
        d.mkdir(parents=True, exist_ok=True)
    return dirs

def sha256sum(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()
