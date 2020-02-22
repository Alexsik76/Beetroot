year = input('Введите год: ')
if not year.isnumeric():
    print('Год содержит не только цифры')
if not len(year) == 4:
    print('Год должен состоять из 4 цифр')
if year.isnumeric() and len(year) == 4:
    num_year = int(year)
    if num_year % 4 != 0:
        print('Это обычный год')
    elif num_year % 100 == 0:
        if num_year % 400 == 0:
            print('Это высокосный год')
        else:
            print('Это обычный год')

    elif num_year % 4 == 0:
        print('Это высокосный год')
    else:
        print('Это обычный год')
