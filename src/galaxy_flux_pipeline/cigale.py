def to_cigale(df, redshift=0.0):
    out=df[['id','FUV','FUV_err','NUV','NUV_err','g','g_err','r','r_err','z','z_err']].copy()
    out.insert(1,'redshift',redshift)
    out.columns=['id','redshift','galex.FUV','galex.FUV_err','galex.NUV','galex.NUV_err','decals.g','decals.g_err','decals.r','decals.r_err','decals.z','decals.z_err']
    return out
