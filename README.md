# Galaxy Flux Pipeline (galflux)

`galflux` is a modular, installable Python pipeline for **resolved UV+optical galaxy photometry** using **GALEX FUV/NUV** and **DECaLS g/r/z**.

Bundled demonstration targets used across examples, configs, and docs:
- **UGC 9024**
- **NGC 6902**

## Project scope

This repository is designed for reproducible, WCS-aware resolved photometry workflows with explicit provenance and transparent assumptions.

### Implemented now
- Installable Python package with CLI entry points.
- Config-driven target handling and SIMBAD-assisted coordinate resolution.
- GALEX product query/filter bookkeeping utilities.
- Exposure-weighted stacking utilities.
- Segmentation+morphology masking with galaxy-center protection.
- PSF matching with explicit approximate uncertainty propagation.
- Grid/cell photometry helpers and CIGALE export helper.
- Synthetic deterministic tests for core algorithms.
- Manuscript-style technical documentation in `docs/`.

### Approximate or future improvements
- Field-dependent empirical PSF kernels for all bands.
- Full mission-specific GALEX/DECaLS noise modeling in all product variants.
- Cross-matched external contaminant catalogs (e.g., Gaia) as default mask prior.
- Expanded online integration tests exercising remote services.

---

## Installation

```bash
python -m pip install -e .
python -m pip install -e .[test]
```

Optional conda setup:
```bash
conda env create -f environment.yml
conda activate galflux
python -m pip install -e .
```

---

## Quickstart commands

Resolve example targets:
```bash
galflux resolve-targets --input data/examples/targets_example.csv --config configs/default.yaml
```

Single-target style run for UGC 9024 settings:
```bash
galflux run-all --input data/examples/targets_with_coords_example.csv --config configs/example_single_ugc9024.yaml
```

Single-target style run for NGC 6902 settings:
```bash
galflux run-all --input data/examples/targets_with_coords_example.csv --config configs/example_single_ngc6902.yaml
```

Batch run:
```bash
galflux run-all --input data/examples/targets_example.csv --config configs/example_batch.yaml
```

---

## Documentation map
- `docs/methodology.md`: equations, data model, and scientific assumptions.
- `docs/science_notes.md`: caveats, limitations, and publication-grade extensions.
- `docs/configuration.md`: parameter-by-parameter guidance.
- `docs/outputs.md`: output schema and file organization.
- `docs/troubleshooting.md`: operational debugging.

---

## Notebook example

A fully explained, plot-rich, synthetic workflow notebook is included at:
- `examples/demo_pipeline_notebook.ipynb`

It demonstrates:
- synthetic galaxy+contaminant scene construction,
- advanced masking behavior,
- PSF matching and integrated flux check,
- exposure-weighted stacking,
- unit conversions.

---

## Output layout

`outputs/<galaxy_id>/{raw,intermediate,masks,psfmatched,reproj,photometry,figures,logs,provenance}`

---

## Acknowledgment / references

See `docs/methodology.md` for method references (GALEX mission calibration paper, Legacy Surveys data paper, and relevant software ecosystem citations).
