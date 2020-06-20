# threading1
import threading
import time
import random


def worker(number):
    thread_name = threading.current_thread().getName()
    for i in range(1000):
        number = i
        time.sleep(0.001)
    print(f"I am Worker {thread_name}, I my number is {number}")


number = 0
t1 = threading.Thread(target=worker, name='t1', args=(number,))
t2 = threading.Thread(target=worker, name='t2', args=(number,))

t1.start()
t2.start()
t1.join()
t2.join()
print('Main thread is finished')
