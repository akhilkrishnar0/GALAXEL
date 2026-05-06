# Galaxy Flux Pipeline (galflux)

`galflux` is a modular, installable Python pipeline for **resolved UV+optical galaxy photometry** using **GALEX FUV/NUV** and **DECaLS g/r/z**.
Bundled demo targets: **UGC 9024** and **NGC 6902**.

## Current implementation status
Fully implemented in this repo:
- package install + CLI + YAML/JSON config
- target-table parsing and SIMBAD-assisted coordinate resolution
- GALEX query/product filtering bookkeeping helpers
- exposure-weighted stacking utilities with reprojection
- segmentation+morphology masking with galaxy-center protection
- PSF smoothing + approximate uncertainty convolution
- grid/cell photometry + CIGALE-format export helpers
- deterministic offline tests with synthetic data

Approximate / future improvements:
- mission-grade GALEX product-type heuristics for all release variants
- full survey-specific DECaLS uncertainty ingest for all layers
- optional external star-catalog cross-matching
- expanded integration tests requiring remote data access

## Install
```bash
python -m pip install -e .[test]
```

## Quickstart
```bash
galflux resolve-targets --input data/examples/targets_example.csv --config configs/default.yaml
```

UGC 9024:
```bash
galflux run-all --input data/examples/targets_with_coords_example.csv --config configs/example_single_ugc9024.yaml
```

NGC 6902:
```bash
galflux run-all --input data/examples/targets_with_coords_example.csv --config configs/example_single_ngc6902.yaml
```

Batch (UGC 9024 + NGC 6902):
```bash
galflux run-all --input data/examples/targets_example.csv --config configs/example_batch.yaml
```

## Output layout
`outputs/<galaxy_id>/{raw,intermediate,masks,psfmatched,reproj,photometry,figures,logs,provenance}`
