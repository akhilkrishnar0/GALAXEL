from __future__ import annotations
from astroquery.mast import Observations

def query_galex_products(ra: float, dec: float, radius_deg: float):
    obs = Observations.query_region(f"{ra} {dec}", radius=f"{radius_deg} deg", obs_collection='GALEX')
    if len(obs)==0:
        return obs, None
    products = Observations.get_product_list(obs)
    return obs, products
