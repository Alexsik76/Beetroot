# threading1
import threading
import time


def worker(number):
    thread_name = threading.current_thread().name
    for i in range(1000):
        number = i
        time.sleep(0.001)
    print(f"I am Worker {thread_name}, my number is {number}\n")


number = 0
t1 = threading.Thread(target=worker, name='t1', args=(number,))
t2 = threading.Thread(target=worker, name='t2', args=(number,))

t1.start()
t2.start()
# t1.join()
# t2.join()
print('Main thread is finished', '\n')
