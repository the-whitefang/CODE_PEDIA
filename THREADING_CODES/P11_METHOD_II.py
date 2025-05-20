# Write a function that computes the square of numbers from 1 to 5.
# Run this function in three separate threads and ensure all threads
# execute in parallel.
# METHOD II

import threading
import math
import time

def square_numbers(start, end):
    for i in range(start, end):
        print(int(math.pow(i, 2)))
    time.sleep(1)

# Define thread ranges
ranges = [(1, 3), (3, 5), (5, 6)]

# Create and start threads
threads = [threading.Thread(target=square_numbers, args=r) for r in ranges]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
