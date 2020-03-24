from datetime import datetime
start = input('Введіть час початку: ')
finish = input('Введіть час закінчення: ')
t4 = datetime.strptime(start, '%H:%M')
t5 = datetime.strptime(finish, '%H:%M')
delta = t5 - t4


def last_letter(number):
    last_number = int(str(number)[-1])
    if last_number == 1:
        last_letter = 'у'
    elif 1 < last_number < 5:
        last_letter = 'и'
    else:
        last_letter = ''
    return last_letter


x = datetime.strptime(str(delta), '%H:%M:%S')
hll = last_letter(x.hour)
mll = last_letter(x.minute)
first_text = 'надавалась ' if (x.hour > 0 or x.minute > 0) else 'не надавалась'
hour_text = f'{str(x.hour)} годин{hll}, ' if x.hour > 0 else ''
min_text = f'{str(x.minute)} хвилин{mll}.' if x.minute > 0 else '.'
print(f'Послуга {first_text}{hour_text}{min_text}')
