import numpy as np
from galaxy_flux_pipeline.validation import flux_stats

def test_flux_stats():
    s=flux_stats(np.array([1,2,3]),np.array([1,2,3]))
    assert abs(s['mean'])<1e-12
