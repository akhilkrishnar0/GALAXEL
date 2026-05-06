from pathlib import Path
import matplotlib.pyplot as plt

def save_band_figure(data_dict,outdir:Path,prefix='bands'):
    outdir.mkdir(parents=True,exist_ok=True)
    fig,ax=plt.subplots(1,len(data_dict),figsize=(4*len(data_dict),4))
    for i,(b,d) in enumerate(data_dict.items()):
        a=ax[i] if len(data_dict)>1 else ax
        im=a.imshow(d,origin='lower',cmap='magma'); a.set_title(b); plt.colorbar(im,ax=a)
    fig.tight_layout();
    for ext in ['png','pdf']: fig.savefig(outdir/f'{prefix}.{ext}',dpi=200)
    plt.close(fig)
