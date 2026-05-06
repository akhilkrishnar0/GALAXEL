from __future__ import annotations
import argparse
from pathlib import Path
from .config import load_config
from .io import read_targets, sanitize_galaxy_id
from .target_resolution import resolve_targets


def cmd_resolve(args):
    cfg = load_config(args.config)
    df = read_targets(args.input)
    out = resolve_targets(df, validate_if_both=cfg.validate_name_coords, tol_arcsec=cfg.name_coord_tolerance_arcsec)
    p = Path(cfg.output_root) / "resolved_targets.csv"
    p.parent.mkdir(exist_ok=True, parents=True)
    out.to_csv(p, index=False)
    print(p)


def cmd_run_all(args):
    cmd_resolve(args)


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="galflux")
    sub = p.add_subparsers(dest="cmd", required=True)
    for name, fn in [
        ("resolve-targets", cmd_resolve),
        ("download", cmd_run_all),
        ("process", cmd_run_all),
        ("validate", cmd_run_all),
        ("export-cigale", cmd_run_all),
        ("make-figures", cmd_run_all),
        ("run-all", cmd_run_all),
    ]:
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
