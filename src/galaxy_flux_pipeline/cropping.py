from astropy.nddata import Cutout2D
from astropy.coordinates import SkyCoord
import astropy.units as u

def crop_to_size(data,wcs,ra,dec,size_arcsec):
    c=SkyCoord(ra,dec,unit='deg')
    return Cutout2D(data,position=c,size=size_arcsec*u.arcsec,wcs=wcs,mode='trim')
