# simple
try:
    1 / 0
except ZeroDivisionError:
    print('1 imposible operation')

# lambda
try:
    (lambda x, y: x / y)(2, 0)
except ZeroDivisionError:
    print('2 imposible operation')


def division(x, y):
    try:
        x / y
    except ZeroDivisionError:
        print('3 imposible operation')


(lambda x, y: division(x, y))(2, 0)
