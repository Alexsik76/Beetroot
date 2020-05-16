class Person:
    number_on_lesson = 0
    list_on_lesson = []
    all_have_money = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__have_money = 10

    def go_to_lesson(self):
        print(f'{self.name} пішов на лекцію.')
        Person.number_on_lesson += 1
        Person.list_on_lesson.append(self.name)
        Person.all_have_money += self.__have_money

    def go_home(self):
        print(f'{self.name} пішов додому.')
        Person.number_on_lesson -= 1
        Person.list_on_lesson.remove(self.name)
        Person.all_have_money -= self.__have_money

    @staticmethod
    def how_much():
        print(f'Всього на лекції {Person.number_on_lesson}')

    @staticmethod
    def who_on_lesson():
        print('Сьогодні на лекції присутні:')
        for item in Person.list_on_lesson:
            print(f'{item}')
        Person.how_much()

    @staticmethod
    def display_money():
        print(f'У присутніх на лекції всього {Person.all_have_money} грошей')


persons = []
persons.append(Person('Vova', 13))
persons.append(Person('Julia', 22))
persons.append(Person('Serg', 25))
persons[1].go_to_lesson()
persons[2].go_to_lesson()
Person.display_money()
Person.who_on_lesson()
Person.go_to_lesson(persons[0])
Person.who_on_lesson()
Person.display_money()
persons[0].go_home()
Person.who_on_lesson()
Person.display_money()
