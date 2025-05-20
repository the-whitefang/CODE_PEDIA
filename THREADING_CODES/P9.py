# Create a program where three threads each print a greeting message (e.g.,
# "Hello from Thread 1", "Hello from Thread 2") with a delay of 1 second
# between messages.

import threading
import time

def Print_Hello(i):
  print(f"Hello from Thread {i}")
  time.sleep(1)

thread1 = threading.Thread(target=Print_Hello(1), name= "Thread-1")
thread2 = threading.Thread(target=Print_Hello(2), name= "Thread-2")
thread3 = threading.Thread(target=Print_Hello(3), name= "Thread-3")

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

