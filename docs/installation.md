# Installation

## Requirements
- Python 3.10+
- pip or conda/mamba

## Pip install
```bash
python -m pip install -e .
python -m pip install -e .[test]
```

## Conda install
```bash
conda env create -f environment.yml
conda activate galflux
python -m pip install -e .
```

## Verify
```bash
galflux --help
pytest -q
```

If dependency installation fails in restricted environments, preinstall wheels from a trusted mirror and then run editable install.
