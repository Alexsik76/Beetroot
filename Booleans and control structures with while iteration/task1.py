word = input('Введите слово: ')
if len(word) < 2:
    print('Empty String')
else:
    res_word = word[:2] + word[-2:]
    print(f'Результат: {res_word}')
