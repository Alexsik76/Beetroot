import timeit
from time import time


def sequential_search(array, item):
    pos = 0
    found = False
    while pos < len(array) and not found:
        if array[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


def sequential_search_2(array, item):
    for i in array:
        if i == item:
            return True
    return False


def simple_search(array, item):
    return item in array


def binary_search(array, item):
    first = 0
    last = len(array) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if array[midpoint] == item:
            found = True
        else:
            if item < array[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


if __name__ == "__main__":
    arr = [-100, -1.5, 2, 3, 4, 6, 31, 101]
    item = 6
    seq_timer = timeit.timeit(
        stmt=f"sequential_search({arr}, {item})",
        setup="from __main__ import sequential_search"
    )
    print(seq_timer)

    seq2_timer = timeit.timeit(
        stmt=f"sequential_search_2({arr}, {item})",
        setup="from __main__ import sequential_search_2"
    )
    print(seq2_timer)

    simple_timer = timeit.timeit(
        stmt=f"simple_search({arr}, {item})",
        setup="from __main__ import simple_search"
    )
    print(simple_timer)

    bin_timer = timeit.timeit(
        stmt=f"binary_search({arr}, {item})",
        setup="from __main__ import binary_search"
    )
    print(bin_timer)


    def my_time(func):
        start = time()
        func([-100, -1.5, 2, 3, 4, 6, 31, 101], 3)
        stop = time()
        print((stop - start) * 1000000)


    print('My_time')
    print('=' * 80)
    my_time(sequential_search)
    my_time(sequential_search_2)
    my_time(simple_search)
    my_time(binary_search)

