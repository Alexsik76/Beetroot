from datetime import datetime
start = input('Введіть час початку: ')
finish = input('Введіть час закінчення: ')
t4 = datetime.strptime(start, '%H:%M')
t5 = datetime.strptime(finish, '%H:%M')
print(t4)
print(t5)
t1 = t5 - t4
print(str(t1))
# x = t1.total_seconds()
x = datetime.strptime(str(t1), '%H:%M:%S')
h = x.hour
m = x.minute
print(f'Послуга надавалась {x.hour} годин(и), {x.minute} хвилин(и)')
