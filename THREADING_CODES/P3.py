# Running Multiple Threads
import threading


def sum_diff(a,b):
  sum = a + b
  diff = a - b
  print(f"Sum of two numbers: {sum}")
  print(f"Difference of two numbers: {diff}")

thread0 = threading.Thread(target=sum_diff(120,80), name="Thread-0")
thread4 = threading.Thread(target=sum_diff(140,70), name="Thread-4")

thread0.start()
thread4.start()

print("Main thread executing. . .")

thread0.join()
thread4.join()

print("Both theads have completed execution.")