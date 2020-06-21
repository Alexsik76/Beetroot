import threading


def counter(number):
    for i in range(number):
        x = i
    print(x)


def threads_task(number):
    number = int(number / 2)
    t1 = threading.Thread(target=counter, args=(number,))
    t2 = threading.Thread(target=counter, args=(number,))

    # start threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()


def single_task(number):
    counter(number)


number = 10_000_000
# threads_task(number)
single_task(number)
