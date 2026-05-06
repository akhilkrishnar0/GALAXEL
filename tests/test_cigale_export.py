import pandas as pd
from galaxy_flux_pipeline.cigale import export_cigale

def test_export_cols():
    df=pd.DataFrame([{"id":1,"FUV":1,"FUV_err":.1,"NUV":1,"NUV_err":.1,"g":1,"g_err":.1,"r":1,"r_err":.1,"z":1,"z_err":.1}])
    out=export_cigale(df)
    assert 'galex.FUV' in out.columns
