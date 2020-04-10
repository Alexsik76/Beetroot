def get_temp_description(temp):
    return {
               temp < -20: 'Холодно',
        -20 <= temp < 0:   'Прохладно',
          0 <= temp < 15:  'Зябко',
         15 <= temp < 25:  'Тепло',
         25 <= temp:       'Жарко'
    }[True]

rez = get_temp_description(26)
print(rez)
d = {1: 'Ok', 2: 'No', 0: 'Error'}
print(d[False])