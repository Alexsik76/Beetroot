# Write a function called oops that explicitly raises an IndexError exception
# when called. Then write another function that calls oops inside a try/except
# state­ment to catch the error. What happens if you change oops to raise
# KeyError instead of IndexError?


def oops():
    raise IndexError


def another_function():
    try:
        oops()
    except IndexError:
        print('error1')


another_function()


def oops1():
    raise KeyError


def another_function1():
    try:
        oops1()
    except (IndexError, KeyError):
        print('error2')


another_function1()
