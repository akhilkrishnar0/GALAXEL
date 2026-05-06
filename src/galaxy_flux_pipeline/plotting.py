from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def _save(fig: plt.Figure, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path.with_suffix('.png'), dpi=220)
    fig.savefig(path.with_suffix('.pdf'))
    plt.close(fig)


def save_image(data: np.ndarray, path: Path, title: str, unit: str = "") -> None:
    fig, ax = plt.subplots(figsize=(5, 4), dpi=180)
    im = ax.imshow(data, origin='lower', cmap='magma')
    ax.set_title(title)
    c = fig.colorbar(im, ax=ax)
    c.set_label(unit)
    _save(fig, path)


def save_band_panels(images: dict[str, np.ndarray], path: Path, unit: str = "") -> None:
    bands = list(images.keys())
    n = len(bands)
    fig, axs = plt.subplots(1, n, figsize=(4*n, 4), dpi=180)
    axs = np.atleast_1d(axs)
    for ax, b in zip(axs, bands):
        im = ax.imshow(images[b], origin='lower', cmap='magma')
        ax.set_title(b)
        ax.set_xticks([]); ax.set_yticks([])
        c = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        c.set_label(unit)
    _save(fig, path)


def save_mask_overlay(image: np.ndarray, mask: np.ndarray, path: Path, title: str = "Mask overlay") -> None:
    fig, ax = plt.subplots(figsize=(5, 4), dpi=180)
    ax.imshow(image, origin='lower', cmap='gray')
    ax.contour(mask.astype(float), levels=[0.5], colors='cyan', linewidths=0.8)
    ax.set_title(title)
    ax.set_xticks([]); ax.set_yticks([])
    _save(fig, path)


def save_psf_comparison(before: np.ndarray, after: np.ndarray, path: Path) -> None:
    fig, axs = plt.subplots(1, 2, figsize=(10, 4), dpi=180)
    for ax, arr, ttl in zip(axs, [before, after], ["Before PSF match", "After PSF match"]):
        im = ax.imshow(arr, origin='lower', cmap='magma')
        ax.set_title(ttl)
        ax.set_xticks([]); ax.set_yticks([])
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    _save(fig, path)
