for i in range(0, 101):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Bizz')