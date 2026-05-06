from pathlib import Path
import json, datetime

def log_provenance(path:Path, stage:str, payload:dict):
    path.parent.mkdir(parents=True,exist_ok=True)
    rec={'timestamp':datetime.datetime.utcnow().isoformat(),'stage':stage,'payload':payload}
    with path.open('a') as f: f.write(json.dumps(rec)+'\n')
