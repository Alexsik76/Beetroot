# Method overloading
class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print('woof woof')


class Cat(Animal):
    def talk(self):
        print('meow')


def f(instance):
    print(instance.__class__.__name__, ' say:')
    instance.talk()


long = Dog()
loki = Cat()

f(long)
f(loki)
