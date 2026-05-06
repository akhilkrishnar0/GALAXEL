import numpy as np

def build_cell_grid(shape,cell_pix):
    ny,nx=shape
    ys=np.arange(0,ny,cell_pix); xs=np.arange(0,nx,cell_pix)
    return [(x,y,min(x+cell_pix,nx),min(y+cell_pix,ny)) for y in ys for x in xs]
