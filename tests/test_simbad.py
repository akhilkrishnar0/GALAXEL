import pandas as pd
from galaxy_flux_pipeline.target_resolution import resolve_targets

def test_resolve_skips_when_coords_present():
    df=pd.DataFrame([{'galaxy_name':'UGC 9024','ra':1.0,'dec':2.0,'distance_mpc':10}])
    out=resolve_targets(df)
    assert out.loc[0,'ra']==1.0
