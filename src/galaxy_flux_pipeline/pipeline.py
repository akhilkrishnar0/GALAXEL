from pathlib import Path
import numpy as np
from .config import load_config
from .io import read_targets, ensure_dirs
from .target_resolution import resolve_targets
from .provenance import log_provenance

def run_all(input_path:str, config_path:str):
    cfg=load_config(config_path); df=resolve_targets(read_targets(input_path))
    root=Path('outputs')
    for _,row in df.iterrows():
        d=ensure_dirs(root,row['galaxy_id'])
        log_provenance(d['provenance']/"pipeline.jsonl", "resolved", row.to_dict())
        np.save(d['intermediate']/"dummy.npy", np.array([row['ra'],row['dec'],cfg.crop_size_arcsec]))
    return df
