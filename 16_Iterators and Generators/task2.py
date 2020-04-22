def in_range(start: int, end: int, step=1):
    if step != 0:
        j = start
        while start < (j + step) <= end:
            yield j
            j += step
    else:
        error_string = 'Arg 3 must not be zero'
        print(f'\033[31m{error_string}\033[0m')


for i in in_range(2, 20, 3):
    print(i)
for i in range(2, 20, 3):
    print(i)
