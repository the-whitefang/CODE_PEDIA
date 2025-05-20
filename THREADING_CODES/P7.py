from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
  print(f"Task {name} is running.")
  time.sleep(2)
  print(f"Task{name} completed.")

with ThreadPoolExecutor(max_workers=3) as executor:
  for i in range(5):
    executor.submit(task, i)

print("All tasks submitted.")