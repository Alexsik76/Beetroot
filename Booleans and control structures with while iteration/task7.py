import random
curent_temp = random.randint(-25, 35)
print('T = ' + str(curent_temp))
if curent_temp > 27:
    print('Я иду на пляж')
elif 18 < curent_temp < 28:
    print('Я иду гулять')
elif 10 < curent_temp < 19:
    print('Я иду гулять в шапке')
elif 0 < curent_temp < 11:
    print('Я иду гулять в пальто и шапке')
else:
    print('Я сижу дома')
