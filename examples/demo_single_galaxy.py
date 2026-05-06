from pathlib import Path
import subprocess
subprocess.run(["galflux","run-all","--input","data/examples/targets_example.csv","--config","configs/default.yaml"],check=False)
print(Path('outputs').resolve())
