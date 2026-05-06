# Quickstart

## 1) Resolve names to coordinates (UGC 9024 + NGC 6902)
```bash
galflux resolve-targets --input data/examples/targets_example.csv --config configs/default.yaml
```

## 2) Single-galaxy example (UGC 9024)
```bash
galflux run-all --input data/examples/targets_with_coords_example.csv --config configs/example_single_ugc9024.yaml
```

## 3) Single-galaxy example (NGC 6902)
```bash
galflux run-all --input data/examples/targets_with_coords_example.csv --config configs/example_single_ngc6902.yaml
```

## 4) Batch example
```bash
galflux run-all --input data/examples/targets_example.csv --config configs/example_batch.yaml
```

## 5) Validate outputs
Inspect `outputs/*/provenance` and `outputs/*/figures` for QA.
See README for commands. This document details quickstart for UGC 9024 and NGC 6902 workflows.
