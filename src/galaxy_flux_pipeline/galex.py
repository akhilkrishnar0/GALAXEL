from astroquery.mast import Observations
from pathlib import Path

def query_galex(ra,dec,radius_deg=0.2):
    return Observations.query_region(f"{ra} {dec}", radius=f"{radius_deg} deg")

def select_galex_products(obs):
    ids=obs['obsid'] if len(obs) else []
    if len(ids)==0: return None
    products=Observations.get_product_list(obs)
    wanted=products[[('int' in str(u).lower() or 'cnt' in str(u).lower()) for u in products['productFilename']]]
    return wanted

def download_products(products,outdir:Path):
    if products is None: return []
    m=Observations.download_products(products,mrp_only=False,download_dir=str(outdir))
    return m
