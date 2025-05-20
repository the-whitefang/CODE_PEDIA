# Write a Python program where Thread-1 prints even numbers from 0 to 10,
# and Thread-2 prints odd numbers from 1 to 9.

import threading

def even_numbers():
  list1 = []
  for i in range(0,10):
    if i % 2 == 0:
      list1.append(i)
  print(f"List of Even Numbers from 1 to 10 = {list1}")
  print()

def odd_numbers():
  list2 = []
  for j in range(1,9):
    if j % 2 != 0:
      list2.append(j)
  print(f"List of Odd Number from 1 to 9 = {list2}")
  print()


thread1 = threading.Thread(target=even_numbers, name="Thread-1")
thread2 = threading.Thread(target=odd_numbers, name="Thread-2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()