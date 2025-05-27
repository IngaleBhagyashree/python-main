import time
import subprocess

python_files = ["file1.py", "file2.py", "file3.py", "file4.py"]

for file in python_files:
    print(f"Running {file}...")
    subprocess.run(["python", file])
    time.sleep(2)  # wait 2 seconds before next