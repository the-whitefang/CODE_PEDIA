import threading
import time

class MyThread(threading.Thread):
  def run(self):
    for i in range(3):
      print(f"{self.name} - Count: {i}")
      time.sleep(1)


thread2 = MyThread(name="Worker_1")
thread5 = MyThread(name="Worker_2")

thread2.start()
thread5.start()

thread2.join()
thread5.join()

print("All Thread finished execution!")