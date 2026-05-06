from __future__ import annotations
import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u
from .simbad_utils import resolve_name

def resolve_targets(df: pd.DataFrame, validate_if_both: bool = True, tol_arcsec: float = 10.0) -> pd.DataFrame:
    rows=[]
    for _,r in df.iterrows():
        name = r.get('galaxy_name')
        ra,dec = r.get('ra'),r.get('dec')
        if pd.isna(ra) or pd.isna(dec):
            if pd.isna(name):
                raise ValueError('Need name or coordinates')
            s = resolve_name(str(name))
            rows.append({**r.to_dict(),"ra":s['ra'],"dec":s['dec'],"resolved_from":"simbad"})
        else:
            rows.append({**r.to_dict(),"resolved_from":"input"})
            if validate_if_both and isinstance(name,str) and name.strip():
                try:
                    s=resolve_name(name)
                    c0=SkyCoord(float(ra),float(dec),unit='deg')
                    c1=SkyCoord(s['ra'],s['dec'],unit=(u.hourangle,u.deg))
                    rows[-1]['name_coord_sep_arcsec']=c0.separation(c1).arcsec
                    rows[-1]['name_coord_match']=rows[-1]['name_coord_sep_arcsec']<=tol_arcsec
                except Exception:
                    rows[-1]['name_coord_match']=False
    return pd.DataFrame(rows)
