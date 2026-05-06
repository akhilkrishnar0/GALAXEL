import argparse
from .pipeline import run_all

def main():
    p=argparse.ArgumentParser(prog='galflux')
    sub=p.add_subparsers(dest='cmd',required=True)
    for c in ['resolve-targets','download','process','validate','export-cigale','make-figures','run-all']:
        s=sub.add_parser(c); s.add_argument('--input',required=True); s.add_argument('--config',required=True)
    a=p.parse_args()
    run_all(a.input,a.config)

if __name__=='__main__':
    main()
