import pandas as pd
from galaxy_flux_pipeline.photometry import convert_to_mjy

def test_conversion_positive():
    df=pd.DataFrame([{'FUV':1,'FUV_err':.1,'NUV':1,'NUV_err':.1,'g':1,'g_err':.1,'r':1,'r_err':.1,'z':1,'z_err':.1}])
    out=convert_to_mjy(df)
    assert out.loc[0,'g']>0
