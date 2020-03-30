# School


class Person:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def hello(self):
        print('Hello')

    def introduce(self):
        string_introduce = f"My name is {self.name}. I'm {self.age} years old."
        print(string_introduce)


class Teacher(Person):
    def __init__(self, name, age, school, specialty, salary):
        super().__init__(name, age, school)
        self.specialty = specialty
        self.salary = salary

    def introduce(self):
        string_introduce = f"My name is {self.name}.\nI'm {self.age} years old.\nMy specialty is {self.specialty}."
        print(string_introduce)


class Student(Person):
    def __init__(self, name, age, school, class_number=None):
        super().__init__(name, age, school)
        self.class_number = class_number
        self.class_number = self.get_class_number()

    def get_class_number(self):
        if not self.class_number:
            return self.age - 6

    def introduce(self):
        string_introduce = (f"My name is {self.name}.\n"
                            f"I'm {self.age} years old.\n"
                            f"I'm student of the {self.class_number}'th class."
                            )
        print(string_introduce)


v = Student('Vova', 13, 'Number 3')
v.introduce()
