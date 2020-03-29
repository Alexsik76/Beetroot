import csv
from random import randint


def random_value(value):
    return randint((value - int(value/10)), (value + int(value/10)))


class Vehicles:
    min_sp = None
    max_sp = None
    min_pow = None
    max_pow = None

    def __init__(self, wheels, speed, power, random=False):
        self.random = random
        self.wheels = wheels
        self.speed = speed
        self.power = power
        self.speed_power(random)

    def speed_power(self, random):
        if random:
            self.speed = random_value(self.speed)
            self.power = random_value(self.power)
            print(self.speed)
        else:
            self.speed = self.speed
            self.power = self.power
            print(self.speed)
    @property
    def description(self):
        rez = f'\n{self.__class__.__name__}\nwheels: {self.wheels}\n speed: {self.speed}\n power: {self.power}\n'
        return rez

    def intervals(self):
        i_sp = int(self.speed / 10)
        i_pow = int(self.power / 10)
        self.min_sp = self.speed - i_sp
        self.max_sp = self.speed + i_sp
        self.min_pow = self.speed - i_pow
        self.max_pow = self.speed + i_pow

    def comparison(self, obj):
        self.intervals()
        if (obj[0] == self.wheels
                and self.min_sp <= obj[1] <= self.max_sp
                and self.min_pow <= obj[1] <= self.max_pow):
            print(f'{self.min_sp} , {obj[1]} , {self.max_sp}')
            return True


class Bikes(Vehicles):
    def __init__(self, wheels, speed, power, random=False):
        super().__init__(wheels, speed, power, random)


class Cars(Vehicles):
    def __init__(self, wheels, speed, power, random=False):
        super().__init__(wheels, speed, power, random)


class Buses(Vehicles):
    def __init__(self, wheels, speed, power, random=False):
        super().__init__(wheels, speed, power, random)


class Trucks(Vehicles):
    def __init__(self, wheels, speed, power, random=False):
        super().__init__(wheels, speed, power, random)


# last Classes


class PedalBikes(Bikes):
    def __init__(self, wheels=2, speed=20, power=0.5, random=False):
        super().__init__(wheels, speed, power, random)


class MotorBikes(Bikes, Cars):
    def __init__(self, wheels=2, speed=180, power=200, random=False):
        super().__init__(wheels, speed, power, random)


class PickUps(Cars):
    def __init__(self, wheels=4, speed=80, power=90, random=False):
        super().__init__(wheels, speed, power, random)


class SportCars(Cars):
    def __init__(self, wheels=4, speed=300, power=500, random=False):
        super().__init__(wheels, speed, power, random)


class EstateCars(Cars):
    def __init__(self, wheels=4, speed=200, power=200, random=False):
        super().__init__(wheels, speed, power, random)


class MediumTrucks(Trucks):
    def __init__(self, wheels=6, speed=130, power=250, random=False):
        super().__init__(wheels, speed, power, random)


class HeavyTrucks(Trucks):
    def __init__(self, wheels=8, speed=111, power=800, random=False):
        super().__init__(wheels, speed, power, random)


# b1 = PedalBikes()
# print(b1.description)
# ht1 = HeavyTrucks(8, 100, 900)
# print(ht1.description)
# print(dir(ht1))
# print(PedalBikes().__class__.__name__)
#

h = HeavyTrucks(random=True)
print(h.speed, h.power)
