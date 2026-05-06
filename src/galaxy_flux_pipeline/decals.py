from pathlib import Path
import requests,hashlib
URL_TEMPLATE_FITS="https://www.legacysurvey.org/viewer/cutout.fits?ra={ra}&dec={dec}&pix={pix}&layer={layer}&size={size}"

def download_decals(ra,dec,outdir:Path,size=512,pix=0.25,layer='ls-dr10'):
    url=URL_TEMPLATE_FITS.format(ra=ra,dec=dec,pix=pix,layer=layer,size=size)
    r=requests.get(url,timeout=90); r.raise_for_status()
    fp=outdir/'decals_grz.fits'; fp.write_bytes(r.content)
    (outdir/'decals_grz.fits.sha256').write_text(hashlib.sha256(r.content).hexdigest())
    return fp,url
