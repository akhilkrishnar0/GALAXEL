from __future__ import annotations
from astroquery.simbad import Simbad

def resolve_name(name: str) -> dict:
    tbl = Simbad.query_object(name)
    if tbl is None or len(tbl)==0:
        raise ValueError(f"SIMBAD could not resolve {name}")
    return {"galaxy_name": name, "ra": tbl['RA'][0], "dec": tbl['DEC'][0], "otype": str(tbl['OTYPE'][0]) if 'OTYPE' in tbl.colnames else None}
