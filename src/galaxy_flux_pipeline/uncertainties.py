import numpy as np

def ivar_to_sigma(ivar):
    return np.divide(1.0,np.sqrt(ivar),out=np.full_like(ivar,np.nan,dtype=float),where=ivar>0)
