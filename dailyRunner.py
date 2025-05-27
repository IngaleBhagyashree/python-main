import schedule
import time
import subprocess

def run_all_scripts():
    scripts = ["file1.py", "file2.py", "file3.py", "file4.py"]
    for script in scripts:
        print(f"Running {script}...")
        subprocess.run(["python", script])

# Schedule the task at 5:05 PM every day
schedule.every().day.at("17:05").do(run_all_scripts)

print("Scheduler started... Waiting for 5:05 PM")

while True:
    schedule.run_pending()
    time.sleep(60)  # check every minute
