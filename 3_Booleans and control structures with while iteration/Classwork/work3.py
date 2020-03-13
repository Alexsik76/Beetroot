year = input('Введите год своего рождения: ')
if not year.isnumeric():
    print('Год содержит не только цифры')
if not len(year) == 4:
    print('Год должен состоять из 4 цифр')
if year.isnumeric() and len(year) == 4:
    age = 2020 - int(year)
    if age >= 18:
        print('Вы совершеннолетний')
    else:
        print('Вы несовершеннолетний')
