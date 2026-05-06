from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

def save_image(data: np.ndarray, path: Path, title: str, unit: str=""):
    fig,ax=plt.subplots(figsize=(5,4),dpi=200)
    im=ax.imshow(data,origin='lower',cmap='magma')
    ax.set_title(title)
    c=fig.colorbar(im,ax=ax); c.set_label(unit)
    fig.tight_layout(); fig.savefig(path.with_suffix('.png')); fig.savefig(path.with_suffix('.pdf')); plt.close(fig)
