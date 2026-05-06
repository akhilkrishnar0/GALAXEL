from reproject import reproject_interp

def reproject_flux(data,in_wcs,out_wcs,shape_out):
    arr,fp=reproject_interp((data,in_wcs),out_wcs,shape_out=shape_out,return_footprint=True)
    return arr,fp
