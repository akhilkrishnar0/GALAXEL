from galaxy_flux_pipeline.target_resolution import resolve_targets
import pandas as pd

def test_coords_passthrough():
    df=pd.DataFrame([{"galaxy_name":"X","ra":1.0,"dec":2.0,"distance_mpc":10.0}])
    out=resolve_targets(df,validate_if_both=False)
    assert out.loc[0,'resolved_from']=='input'
