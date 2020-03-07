from random import randint
import os
from prettytable import PrettyTable
from time import sleep


class Persona:
    def __init__(self, name):
        self.name = name
    age = 0
    health = 100
    larder = {
                'bananas': [],
                'mangoes': [],
                'apples': [],
                'potatoes': [],
                'wheat': []
              }
    ability = {
                'bananas': 1,
                'mangoes': 1,
                'apples': 1,
                'potatoes': 1,
                'wheat': 1
              }
    using = {
                'bananas': 1,
                'mangoes': 1,
                'apples': 1,
                'potatoes': 1,
                'wheat': 1
            }

    def harvesting(self, day):
        date_of_harvests = [90, 110, 120, 130, 140]
        crops = dict(zip(self.larder.keys(), date_of_harvests))
        for key, value in crops.items():
            # print(f'day = {day}, key = {key}, value = {value}')
            # input()
            if day == value:
                size_of_crops = (310 + randint(-54, 54))
                (self.larder[key]).append(int(size_of_crops * self.ability[key]))

    def get_oldest_product(self, prod):
        if len(self.larder[prod]):
            for nyear in range(len(self.larder[prod])):
                if self.larder[prod][nyear] > 0:
                    self.larder[prod][nyear] -= 1
                    if self.larder[prod][0] == 0:
                        del self.larder[prod][0]
                    return 1
        else:
            return 0

    def nutrition(self):
        ration = 0
        for item in self.larder.keys():
            ration += self.get_oldest_product(item)
        if ration < 4:
            self.health -= (1/365)
        elif ration > 4 and self.health < 100:
            self.health += (1/365)

    def deterioration(self):
        for prod in self.larder.keys():
            if len(self.larder[prod]) > 2:
                for nyear in range(len(self.larder[prod][:-3])):
                    det = int((self.larder[prod][nyear]) / 4)
                    self.larder[prod][nyear] -= det


def create_person(i):
    name = input('Ввведіть ім\'я персонажа: ')
    name = name.replace(' ', '')
    p.append(Persona(name))
    print(f'Створено персонажа {p[i].name}')
    number = 5
    for item in p[i].ability.keys():
        while number > 0:
            # os.system('cls' if os.name == 'nt' else 'clear')
            print("""
            У Вас всього 5 очків навичок.
            Додайте до кожного вміння бажану
            кількість очків.
            """)
            # print(f'У {pers.name} наступні навички:')
            # print(f'')
            for key, value in p[i].ability.items():
                if number > 0:
                    print(f'Залишилось розподілити {number} очків')
                    print(f'Додайте навичку у збиранні {key}:')
                    while True:
                        try:
                            n = int(input())
                            if n < 1 or n > number:
                                raise Exception
                            p[i].ability[key] += (n/10)
                            number -= n
                            break
                        except ValueError:
                            print('Невірный формат')
                        except Exception:
                            print(f'Введіть число від 1 до {number}')
#    print(p[i].name, [i for i in p[i].ability.items()])


def values_of_pers(n, year):
    # generation of a list of propertys of pers
    temp_inf = []
    temp_inf = ([p[n].name,
                p[n].health])
    for key in (p[n].larder).keys():
        temp_inf.append(sum(p[n].larder[key]))
    temp_inf.append(year)
    return temp_inf


def output_pers_inf(year, start=0, stop=2):
    # generation a PrettyTable
    os.system('cls' if os.name == 'nt' else 'clear')
    th = (['Name',
           'Health',
           'bananas',
           'mangoes',
           'apples',
           'potatoes',
           'wheat',
           'Year'])
    table = PrettyTable(th)
    if stop >= 0:
        i = start
        while i < stop:
            table.add_row(values_of_pers(i, year))
            i += 1
    else:
        table.add_row(values_of_pers(start, year))
    print(table)


p = []
for k in range(2):
    create_person(k)
output_pers_inf(0, 2)
# game loop
for year in range(1900, 2001):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        number_of_days = 365
    else:
        number_of_days = 366
    for day in range(1, (number_of_days + 1)):
        for i in range(2):
            p[i].harvesting(day)
            p[i].nutrition()
    for i in range(2):
        p[i].deterioration()

    output_pers_inf(year, 0, 2)
    sleep(1)
    input()
