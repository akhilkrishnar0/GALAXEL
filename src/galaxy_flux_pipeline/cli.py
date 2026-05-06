from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd
from .config import load_config
from .io import read_targets, ensure_dirs
from .target_resolution import resolve_targets


def cmd_resolve(args):
    cfg=load_config(args.config)
    df=read_targets(args.input)
    out=resolve_targets(df)
    p=Path(cfg.output_root)/"resolved_targets.csv"; p.parent.mkdir(exist_ok=True,parents=True)
    out.to_csv(p,index=False)
    print(p)

def cmd_run_all(args):
    cmd_resolve(args)


def parser() -> argparse.ArgumentParser:
    p=argparse.ArgumentParser(prog='galflux')
    sub=p.add_subparsers(dest='cmd',required=True)
    for name,fn in [("resolve-targets",cmd_resolve),("download",cmd_run_all),("process",cmd_run_all),("validate",cmd_run_all),("export-cigale",cmd_run_all),("make-figures",cmd_run_all),("run-all",cmd_run_all)]:
        sp=sub.add_parser(name)
        sp.add_argument('--input',required=True)
        sp.add_argument('--config',required=True)
        sp.set_defaults(func=fn)
    return p

def main():
    p=parser(); a=p.parse_args(); a.func(a)

if __name__=='__main__':
    main()
