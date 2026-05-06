from astropy.wcs import WCS

def make_simple_wcs(nx=100,ny=100,pixscale=0.0002777778,ra=0,dec=0):
    w=WCS(naxis=2); w.wcs.crpix=[nx/2,ny/2]; w.wcs.cdelt=[-pixscale,pixscale]; w.wcs.crval=[ra,dec]; w.wcs.ctype=['RA---TAN','DEC--TAN']; return w
