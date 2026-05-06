import pandas as pd
from .simbad_utils import resolve_name

def resolve_targets(df:pd.DataFrame, validate=False, tolerance_arcsec=10.0)->pd.DataFrame:
    rows=[]
    for _,r in df.iterrows():
        ra,dec=r.get('ra'),r.get('dec')
        name=r.get('galaxy_name')
        if pd.isna(ra) or pd.isna(dec):
            if pd.isna(name): raise ValueError('Need name or coordinates')
            ra2,dec2,_=resolve_name(str(name))
            ra,dec=ra2,dec2
        rows.append({**r.to_dict(),'ra':float(ra),'dec':float(dec),'galaxy_id': str(name) if not pd.isna(name) else f"J{ra:.4f}_{dec:.4f}"})
    return pd.DataFrame(rows)
