def except_decorator(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError as string:
            print(string)
    return wrapper


@except_decorator
def add(a, b):
    print(a, b)

add(1, 2)