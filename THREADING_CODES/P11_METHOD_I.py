# Write a function that computes the square of numbers from 1 to 5.
# Run this function in three separate threads and ensure all threads
# execute in parallel.
# METHOD I

import threading
import math
import time

def square1():
  for i in range(1,3):
    print(int(math.pow(i,2)))
  time.sleep(1)


def square2():
  for j in range(3,5):
    print(int(math.pow(j,2)))
  time.sleep(1)


def square3():
  for k in range(5,6):
    print(int(math.pow(k,2)))
  time.sleep(1)


thread10 = threading.Thread(target=square1, name="Thread-10")
thread11 = threading.Thread(target=square2, name="Thread-11")
thread12 = threading.Thread(target=square3, name="Thread-12")

thread10.start()
thread11.start()
thread12.start()

thread10.join()
thread11.join()
thread12.join()
