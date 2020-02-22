rating = input('Введите оценку: ')
if not rating.isnumeric():
    print('Оценка содержит не только цифры')
else:
    rat = int(rating)
    if rat < 40:
        print('F')
    elif rat == 40:
        print('E')
    elif rat > 40 and rat < 60:
        print('D')
    elif rat > 59 and rat < 74:
        print('C')
    elif rat > 74 and rat < 90:
        print('B')
    elif rat >= 90:
        print('A')
