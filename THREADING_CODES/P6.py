import threading
import time

counter = 0
lock = threading.Lock()

def increase_counter():
  global counter
  for _ in range(100000):
    with lock:
      counter += 1
thread6 = threading.Thread(target=increase_counter)
thread7 = threading.Thread(target=increase_counter)

thread6.start()
thread7.start()

thread6.join()
thread7.join()

print(f"Final Counter Value: {counter}")