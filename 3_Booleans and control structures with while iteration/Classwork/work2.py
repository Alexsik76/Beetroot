import calendar
year = int(input('Введите год: '))
if calendar.isleap(year):
    print('Это высокосный год')
else:
    print('Это обычный год')
