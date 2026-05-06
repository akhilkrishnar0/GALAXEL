from __future__ import annotations
import numpy as np

def combine_errors(err_maps: list[np.ndarray]) -> np.ndarray:
    return np.sqrt(np.nansum(np.stack([e**2 for e in err_maps]),axis=0))
