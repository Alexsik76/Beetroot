# simple
try:
    1 / 0
except ZeroDivisionError:
    print('imposible operation')

# lambda
try:
    (lambda x, y: x / y)(2, 0)
except ZeroDivisionError:
    print('imposible operation')
