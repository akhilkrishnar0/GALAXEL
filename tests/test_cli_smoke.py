from pathlib import Path
from galaxy_flux_pipeline.cli import main
import sys


def test_cli_run_all(tmp_path, monkeypatch):
    out = tmp_path / 'outputs'
    cfg = tmp_path / 'cfg.yaml'
    cfg.write_text('output_root: "'+str(out)+'"\nvalidate_name_coords: false\n')
    inp = Path('data/examples/targets_with_coords_example.csv')
    monkeypatch.setattr(sys, 'argv', ['galflux', 'run-all', '--input', str(inp), '--config', str(cfg)])
    main()
    assert (out / 'resolved_targets.csv').exists()
