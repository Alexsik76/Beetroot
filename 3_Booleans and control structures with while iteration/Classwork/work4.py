rating = input('Введите оценку: ')
if not rating.isnumeric():
    print('Оценка содержит не только цифры')
else:
    rat = int(rating)
    if rat < 40:
        print('F')
    elif rat == 40:
        print('E')
    elif 40 < rat < 60:
        print('D')
    elif 59 < rat < 74:
        print('C')
    elif 74 < rat < 90:
        print('B')
    elif rat >= 90:
        print('A')
