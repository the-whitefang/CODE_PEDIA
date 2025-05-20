#Write a Python script where a thread runs a countdown timer from
#10 to 0, and another thread prints "Timer is running..." every second until
#the countdown ends.

import threading
import time

def countdown():
  for i in range(10,0,-1):
    print(i)
    time.sleep(1)

def msg():
  for i in range(10,0,-1):
    print("Timer is running. . .")
    time.sleep(1)

threada = threading.Thread(target=countdown, name="Thread-a")
threadb = threading.Thread(target=msg, name="Thread-b")

threada.start()
threadb.start()

threada.join()
threadb.join()