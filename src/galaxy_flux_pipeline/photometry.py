import numpy as np, pandas as pd
NMAGGY_TO_MJY=3.631e-3
FUV_CPS_TO_MJY=1.4e-2
NUV_CPS_TO_MJY=2.06e-2

def integrate_cells(images,errors,cells,wcs):
    rows=[]
    for i,(x0,y0,x1,y1) in enumerate(cells):
        r={'id':i,'x':x0,'y':y0}
        for b in ['FUV','NUV','g','r','z']:
            d=images[b][y0:y1,x0:x1]; e=errors[b][y0:y1,x0:x1]
            r[b]=np.nansum(d); r[f'{b}_err']=np.sqrt(np.nansum(e**2))
        ra,dec=wcs.pixel_to_world_values((x0+x1)/2,(y0+y1)/2); r['ra']=ra; r['dec']=dec
        rows.append(r)
    return pd.DataFrame(rows)

def convert_to_mjy(df):
    out=df.copy(); out['g']*=NMAGGY_TO_MJY; out['r']*=NMAGGY_TO_MJY; out['z']*=NMAGGY_TO_MJY
    out['g_err']*=NMAGGY_TO_MJY; out['r_err']*=NMAGGY_TO_MJY; out['z_err']*=NMAGGY_TO_MJY
    out['FUV']*=FUV_CPS_TO_MJY; out['FUV_err']*=FUV_CPS_TO_MJY; out['NUV']*=NUV_CPS_TO_MJY; out['NUV_err']*=NUV_CPS_TO_MJY
    return out
