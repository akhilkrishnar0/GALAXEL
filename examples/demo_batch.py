import subprocess
subprocess.run(["galflux","run-all","--input","data/examples/targets_example.csv","--config","configs/example_batch.yaml"],check=False)
