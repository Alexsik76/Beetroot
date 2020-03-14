def division():
    print('returns the value of squared "a" divided by "b"')
    a = int(input('Input a:'))
    b = int(input('Input b:'))
    res = a**2 / b
    return res


try:
    division()
except (ValueError, ZeroDivisionError) as e:
    print(e)
