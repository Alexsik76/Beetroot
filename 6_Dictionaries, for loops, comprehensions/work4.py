from random import randint
from time import sleep
# economy in the 20th century


class Persona:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
    age = 0
    health = 100
    money = 0
    larder = {'meet': 0, 'fruits': 0, 'milk': 0, 'bread': 0}

    # Guideline Daily Amount
    def gda(self):
        if self.age < 18:
            return randint(1500, 2000)
        elif self.age >= 18 and self.sex == 'female':
            return randint(1800, 2200)
        else:
            return randint(2200, 2700)


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
            print('Ваша відповідь не може бути прийнята\n введіть 1 або 2')
    p.append(Persona(name, sex))


p = []
create_user_person()
print(p[0].name,
      p[0].sex,
      p[0].age,
      p[0].health,
      p[0].money,
      p[0].larder,
      p[0].gda(),
      sep=' ,')
