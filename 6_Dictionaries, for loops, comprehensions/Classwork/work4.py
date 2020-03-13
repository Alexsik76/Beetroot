from random import randint
from time import sleep
import os
from prettytable import PrettyTable
from random import choice
from string import ascii_uppercase
from string import ascii_lowercase
import msvcrt
# economy in the 20th century


class Persona:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
    age = 0
    health = 100
    money = 0
    larder = {'meet': 0, 'fruits': 0, 'milk': 0, 'bread': 0}
    craft = 0
    land = 0
    salary = 0
    # calculating income

    def income(self):
        # each unit of the earth brings a random amount
        # of meet, fruits, milk, bread
        meet = self.land * (randint(0, 1))
        fruits = self.land * (randint(0, 50))
        milk = self.land * (randint(0, 30))
        bread = self.land * (randint(0, 3))
        # each unit of the craft brings a random amount
        # of money
        income_money = self.craft * (randint(0, 15))
        # updating the value
        # - products
        temp_products = [bread, milk, fruits, meet]
        for item in self.larder:
            self.larder[item] += temp_products.pop()
        # - money
            self.money += (income_money + self.salary)

    # Guideline Daily Amount

    def gda(self):
        if self.age < 18:
            return randint(1500, 2000)
        elif self.age >= 18 and self.sex == 'female':
            return randint(1800, 2200)
        else:
            return randint(2200, 2700)

    def sale(self, item, price, number):
        if self.larder[item] >= number:
            self.larder[item] -= number
            self.money += (number * price)
        else:
            print('Товар у такій кількості відсутній!')

    def purchase(self, item, price, number):
        if (price * number) >= self.money:
            self.larder[item] += number
            self.money -= (number * price)


def create_user_person():
    name = input('Ввведіть ім\'я персонажа: ')
    name = name.replace(' ', '')
    while True:
        print('\rВвведіть стать персонажа: ', '\n1: чоловіча', '\n2: жіноча')
        sex_in = input('\n:')
        if int(sex_in) == 1:
            sex = 'male'
            print('\nДякую.')
            break
        elif int(sex_in) == 2:
            sex = 'female'
            print('\nДякую.')
            break
        else:
            print('Ваша відповідь не може бути прийнята,\n введіть 1 або 2')
    p.append(Persona(name, sex))
    p[0].money = randint(0, 1000)
    p[0].craft = randint(0, 1000)
    p[0].land = randint(0, 1000)


def create_npc_persons():
    for j in range(1, 101):
        name = (choice(ascii_uppercase) +
                (''.join(choice(ascii_lowercase)
                 for i in range(6))))
        sex_int = randint(1, 2)
        if sex_int == 1:
            sex = 'male'
        else:
            sex = 'female'
        p.append(Persona(name, sex))
        p[j].money = randint(0, 1000)
        p[j].craft = randint(0, 1000)
        p[j].land = randint(0, 1000)


def values_of_pers(n):
    # generation of a list of propertys of pers
    temp_inf = []
    temp_inf = ([p[n].name,
                p[n].sex,
                p[n].age,
                p[n].health,
                p[n].money])
    for item in p[n].larder:
        temp_inf.append(p[n].larder[item])
    return temp_inf


def output_pers_inf(start, stop=5):
    # generation a PrettyTable
    os.system('cls' if os.name == 'nt' else 'clear')
    th = (['Name',
           'Sex',
           'Age',
           'Health',
           'Money',
           'Meet',
           'Fruits',
           'Milk',
           'Bread'])
    table = PrettyTable(th)
    if stop > 0:
        i = start
        while i <= stop:
            table.add_row(values_of_pers(i))
            i += 1
    else:
        table.add_row(values_of_pers(start))
    print(table)


def user_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Допомога - натисніть "?"
    Вийти з гри - настисність "q"
    Продати - натисність "s"
    Купити - натисність "p"
    Вийти з меню - натисніть "e"
    """)
    while True:
        user_input = input(': ')
        if user_input == '?':
            game_help()
        elif user_input == 'q':
            quit()
        elif user_input == 's':
            user_sale()
        elif user_input == 'p':
            user_purchase()
        elif user_input == 'e':
            break


def select_item(list):
    choice = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        temp_list = list
        for item in range(len(temp_list)):
            if item == choice:
                print(f'\n[{temp_list[choice]}]')
            else:
                print(f'\n{temp_list[item]}')
        if ord(msvcrt.getch()) == 115 and choice < len(temp_list):
            choice += 1
        if ord(msvcrt.getch()) == 119 and choice > 0:
            choice -= 1
        if ord(msvcrt.getch()) == 13:
            target = temp_list[choice]
            print(p[1].name)
            break
    return target


def user_sale():
    list1 = list(((p[0].larder).keys()))
    item = select_item(list1)
    price = int(input('Введіть ціну: '))
    number = int(input('Введіть кількість: '))
    purcaser_list = []
    for i in range(1, 11):
        purcaser_list.append(p[i].name)
    print(purcaser_list)
    purcaser = select_item(purcaser_list)
    p[0].sale(item, price, number)
    p[purcaser_list.index(purcaser)].purchase(item, price, number)
    print('Successfull!')


def user_purchase():
    pass


def game_help():

    print('''Можливо, тут колись з'явиться допомога користувачу,
            але не зараз :(''')
    input('Натисність "Enter" для продовження')


p = []
create_user_person()
create_npc_persons()
output_pers_inf(0, 10)
# game loop
for year in range(1900, 2001):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        number_of_days = 365
    else:
        number_of_days = 366
    for day in range(1, (number_of_days + 1)):
        if msvcrt.kbhit():
            user_menu()
        for i in p:
            i.income()
    for i in p:
        i.age += 1
    output_pers_inf(0, 10)
    sleep(1)
