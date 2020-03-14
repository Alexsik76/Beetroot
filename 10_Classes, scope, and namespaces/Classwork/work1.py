class Person:
    number_on_lesson = 0
    list_on_lesson = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def go_to_lesson(self):
        print(f'{self.name} пішов на лекцію.')
        Person.number_on_lesson += 1
        Person.list_on_lesson.append(self.name)

    def how_much():
        print(f'Всього на лекції {Person.number_on_lesson}')

    def who_on_lesson():
        print('Сьогодні на лекції присутні:')
        for item in Person.list_on_lesson:
            print(f'{item}')
        Person.how_much()


persons = []
persons.append(Person('Vova', 13))
persons.append(Person('Julia', 22))
persons.append(Person('Serg', 25))
persons[1].go_to_lesson()
persons[2].go_to_lesson()
Person.who_on_lesson()
