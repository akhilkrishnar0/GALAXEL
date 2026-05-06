from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np
from .config import load_config
from .io import read_targets, sanitize_galaxy_id, ensure_dirs
from .target_resolution import resolve_targets
from .masking import build_mask
from .psf_matching import match_psf
from .plotting import save_band_panels, save_mask_overlay, save_psf_comparison
from .provenance import write_provenance


def _synthetic_images(seed: int = 0) -> dict[str, np.ndarray]:
    rng = np.random.default_rng(seed)
    y, x = np.indices((160, 160))
    base = np.exp(-(((x-80)/18)**2 + ((y-80)/12)**2))
    return {
        "FUV": base + 0.2*np.exp(-(((x-105)/8)**2 + ((y-60)/8)**2)) + 0.02*rng.normal(size=base.shape),
        "NUV": base + 0.08*np.exp(-(((x-55)/10)**2 + ((y-110)/9)**2)) + 0.02*rng.normal(size=base.shape),
        "g": 1.25*base + 0.01*rng.normal(size=base.shape),
        "r": 1.35*base + 0.01*rng.normal(size=base.shape),
        "z": 1.45*base + 0.01*rng.normal(size=base.shape),
    }


def cmd_resolve(args):
    cfg = load_config(args.config)
    df = read_targets(args.input)
    out = resolve_targets(df, validate_if_both=cfg.validate_name_coords, tol_arcsec=cfg.name_coord_tolerance_arcsec)
    p = Path(cfg.output_root) / "resolved_targets.csv"
    p.parent.mkdir(exist_ok=True, parents=True)
    out.to_csv(p, index=False)
    print(p)


def cmd_process(args):
    cfg = load_config(args.config)
    df = resolve_targets(read_targets(args.input), validate_if_both=False)
    for i, row in df.iterrows():
        gid = sanitize_galaxy_id(row.get("galaxy_name"), fallback=f"target_{i}")
        outdir = Path(cfg.output_root) / gid
        dirs = ensure_dirs(outdir)
        imgs = _synthetic_images(seed=i+42)
        save_band_panels(imgs, dirs["figures"] / "raw_band_panels", unit="arb")
        mask, _ = build_mask(imgs["r"], nsigma=cfg.masking["nsigma"], npixels=cfg.masking["npixels"], protect_center_px=cfg.masking["protect_radius_arcsec"] / cfg.decals_pixscale)
        save_mask_overlay(imgs["r"], mask, dirs["figures"] / "mask_overlay")
        psf = match_psf(imgs["g"], current_fwhm=1.3, target_fwhm=cfg.target_psf_fwhm_arcsec, pixscale=cfg.decals_pixscale)
        save_psf_comparison(imgs["g"], psf, dirs["figures"] / "psf_compare")
        write_provenance(dirs["provenance"] / "process.json", {
            "galaxy_id": gid,
            "mode": "synthetic_demo",
            "assumption": "Synthetic arrays used for deterministic offline QA. Replace with survey data for science products.",
            "config": cfg.to_dict(),
        })


def cmd_run_all(args):
    cmd_resolve(args)
    cmd_process(args)


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="galflux")
    sub = p.add_subparsers(dest="cmd", required=True)
    mapping = {
        "resolve-targets": cmd_resolve,
        "download": cmd_process,
        "process": cmd_process,
        "validate": cmd_process,
        "export-cigale": cmd_process,
        "make-figures": cmd_process,
        "run-all": cmd_run_all,
    }
    for name, fn in mapping.items():
        sp = sub.add_parser(name)
        sp.add_argument("--input", required=True)
        sp.add_argument("--config", required=True)
        sp.set_defaults(func=fn)
    return p


def main():
    a = parser().parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
