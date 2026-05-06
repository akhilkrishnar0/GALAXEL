from __future__ import annotations
from pathlib import Path
import json

def write_provenance(path: Path, payload: dict):
    path.write_text(json.dumps(payload,indent=2,sort_keys=True))
