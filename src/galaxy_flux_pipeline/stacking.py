import numpy as np

def exposure_weighted_stack(images,exposures):
    w=np.where(np.isfinite(exposures), exposures,0.0)
    data=np.where(np.isfinite(images),images,0.0)
    ws=w.sum(axis=0)
    img=np.divide((data*w).sum(axis=0),ws,out=np.full(ws.shape,np.nan),where=ws>0)
    err=np.divide(1.0,np.sqrt(ws),out=np.full(ws.shape,np.nan),where=ws>0)
    return img,ws,err
