import threading
import time


print("Main thread continues to execute. . .")
def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers())

thread1.start()

# print("Main thread continues to execute. . .")

thread1.join()
print("Thread execution finished.")