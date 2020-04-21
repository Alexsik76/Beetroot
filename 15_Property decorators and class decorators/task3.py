from functools import wraps


class TypeDecorators:
    @classmethod
    def to_int(cls, func):
        @wraps(func)
        def wrapper(*args):
            value = func(*args)
            if isinstance(value, str) and value.isnumeric():
                return int(value)
            else:
                print("Argument is not string, or is not numeric")

        return wrapper

    @classmethod
    def to_bool(cls, func):
        @wraps(func)
        def wrapper(*args):
            value = func(*args)
            if isinstance(value, str):
                return bool(value)
            else:
                print("Argument is not string")

        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25

assert do_something('True') is True
