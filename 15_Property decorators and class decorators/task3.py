from locale import atof, setlocale, LC_NUMERIC
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
    def to_string(cls, func):
        @wraps(func)
        def wrapper(*args):
            value = func(*args)
            return str(value)

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

    @classmethod
    def to_float(cls, func):
        @wraps(func)
        def wrapper(*args):
            try:
                value = func(*args)
                if '.' in value:
                    setlocale(LC_NUMERIC, 'en_US.UTF-8')
                elif ',' in value:
                    setlocale(LC_NUMERIC, 'uk_UA')
                else:
                    print(f'\033[93mUnknown locale for the float format. Choice "." or ","\033[0m')
                return atof(value)
            except ValueError as error_string:
                print(f'\033[31m{error_string}\033[0m')

        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_float
def do_float(string: str):
    return string


assert do_nothing('25') == 25

assert do_something('True') is True

print(do_float('11,89'))
