from pathlib import Path
import pandas as pd

REQ=["galaxy_name","ra","dec","distance_mpc"]

def read_targets(path:str|Path)->pd.DataFrame:
    df=pd.read_csv(path)
    for c in REQ:
        if c not in df.columns: raise ValueError(f"Missing required column: {c}")
    return df

def ensure_dirs(root:Path, galaxy_id:str)->dict[str,Path]:
    base=root/galaxy_id
    sub=["raw","intermediate","masks","psfmatched","reproj","photometry","figures","logs","provenance"]
    out={s:base/s for s in sub}
    for p in out.values(): p.mkdir(parents=True,exist_ok=True)
    return out
