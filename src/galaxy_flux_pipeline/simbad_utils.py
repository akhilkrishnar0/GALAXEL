from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord
import astropy.units as u

def resolve_name(name:str):
    table=Simbad.query_object(name)
    if table is None: raise ValueError(f"Could not resolve {name}")
    coord=SkyCoord(table['RA'][0], table['DEC'][0], unit=(u.hourangle,u.deg))
    return coord.ra.deg, coord.dec.deg, table
