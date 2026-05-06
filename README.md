# GALAXEL: Resolved GALEX+DECaLS Galaxy Flux Pipeline

Production-oriented Python pipeline for resolved UV+optical photometry using **GALEX FUV/NUV** and **DECaLS g/r/z**. Bundled demonstration targets are **UGC 9024** and **NGC 6902**.

## Features
- SIMBAD target resolution with optional coordinate validation.
- GALEX query/download hooks (MAST) and DECaLS cutout downloads.
- Exposure-weighted stacking, PSF matching, reprojection, and cell photometry.
- CIGALE export, provenance logging, and publication-oriented plots.
- YAML/JSON config support and CLI entrypoint `galflux`.

## Install
```bash
pip install -e .
```
or
```bash
conda env create -f environment.yml
conda activate galflux
pip install -e .
```

## Quickstart
### Batch run (UGC 9024 + NGC 6902)
```bash
galflux run-all --input data/examples/targets_example.csv --config configs/default.yaml
```
### Single galaxy: UGC 9024
```bash
galflux run-all --input data/examples/targets_with_coords_example.csv --config configs/example_single_ugc9024.yaml
```
### Single galaxy: NGC 6902
```bash
galflux run-all --input data/examples/targets_with_coords_example.csv --config configs/example_single_ngc6902.yaml
```

## CLI stages
`resolve-targets`, `download`, `process`, `validate`, `export-cigale`, `make-figures`, `run-all`.

## Outputs
`outputs/<galaxy_id>/{raw,intermediate,masks,psfmatched,reproj,photometry,figures,logs,provenance}`

## Citation/Acknowledgment
Please cite GALEX, Legacy Survey (DECaLS), Astropy, Astroquery, Photutils, and this software.

## Limitations
Network-dependent stages require remote services; tests mock most remote calls.
