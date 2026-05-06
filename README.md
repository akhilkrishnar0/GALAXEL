# Galaxy Flux Pipeline (galflux)

Production-oriented Python pipeline for resolved UV+optical photometry of galaxies using **GALEX FUV/NUV** and **DECaLS g/r/z**.
Bundled demo targets: **UGC 9024** and **NGC 6902**.

## Features
- Single-target and catalog workflows
- SIMBAD resolution with optional coordinate/name consistency checks
- GALEX query + product inspection and DECaLS cutout download
- Exposure-weighted stacking, masking, PSF matching, reprojection, resolved grid photometry
- CIGALE export, provenance logging, QA figures
- CLI + YAML/JSON config + tests

## Install
```bash
pip install -e .
# or
conda env create -f environment.yml && conda activate galflux
```

## Quickstart
```bash
galflux run-all --input data/examples/targets_example.csv --config configs/default.yaml
```

Single-galaxy (UGC 9024):
```bash
galflux run-all --input data/examples/targets_with_coords_example.csv --config configs/example_single_ugc9024.yaml
```
Single-galaxy (NGC 6902):
```bash
galflux run-all --input data/examples/targets_with_coords_example.csv --config configs/example_single_ngc6902.yaml
```
Batch:
```bash
galflux run-all --input data/examples/targets_example.csv --config configs/example_batch.yaml
```

## Outputs
Per galaxy: `outputs/<galaxy_id>/{raw,intermediate,masks,psfmatched,reproj,photometry,figures,logs,provenance}`.

## Notes
Methods are inspired in part by resolved-photometry practices used in projects such as piXedfit, with independent implementation and explicit provenance.
