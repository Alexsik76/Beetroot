# Doggy age
class Dog:
    def __init__(self, dog_age):
        self.age_factor = 7
        self.age = dog_age

    def human_age(self):
        human_age = self.age_factor * self.age
        print(f'If Dog age = {self.age}, Human age = {human_age}')
        return human_age


dog1 = Dog(5)
dog1.human_age()
