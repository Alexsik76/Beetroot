def logger(func):
    def wrapper(*args):
        print(f'{func.__name__} called with {args[0]}', *args[1:], sep=', ')
        return func(*args)
    return wrapper
@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(1, 2)
square_all(1, 2, 3)
