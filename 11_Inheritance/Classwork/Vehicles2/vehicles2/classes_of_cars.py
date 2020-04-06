from random import randint


def random_value(value):
    return randint((value - int(value / 10)), (value + int(value / 10)))


class Vehicles:
    def __init__(self, wheels, speed, power, load_capacity, capacity_of_people, fuel_costs):
        self.wheels = wheels
        self.speed = speed
        self.power = power
        self.load_capacity = load_capacity
        self.capacity_of_people = capacity_of_people
        self.fuel_costs = fuel_costs


    def speed_power(self, random):
        if random:
            self.speed = random_value(self.speed)
            self.power = random_value(self.power)

        else:
            self.speed = self.speed
            self.power = self.power

    @property
    def description(self):
        rez = f'\n{self.__class__.__name__}\nwheels: {self.wheels}\n speed: {self.speed}\n power: {self.power}\n'
        return rez

    def for_csv(self):
        rez = [self.__class__.__name__, self.wheels, self.speed, self.power]
        return rez

    def comparison(self, obj):
        self.intervals()
        if (obj[0] == self.wheels
                and self.min_sp <= obj[1] <= self.max_sp
                and self.min_pow <= obj[2] <= self.max_pow):
            return True


class Bikes(Vehicles):
    def __init__(self, wheels, speed, power, random=True):
        super().__init__(wheels, speed, power, random)


class Cars(Vehicles):
    def __init__(self, wheels, speed, power, random=True):
        super().__init__(wheels, speed, power, random)


class Buses(Vehicles):
    def __init__(self, wheels, speed, power, random=True):
        super().__init__(wheels, speed, power, random)


class Trucks(Vehicles):
    def __init__(self, wheels, speed, power, random=True):
        super().__init__(wheels, speed, power, random)


# last Classes


class PedalBikes(Bikes):
    def __init__(self, wheels=2, speed=20, power=15, random=True):
        super().__init__(wheels, speed, power, random)


class MotorBikes(Bikes, Cars):
    def __init__(self, wheels=2, speed=180, power=200, random=True):
        super().__init__(wheels, speed, power, random)


class PickUps(Cars):
    def __init__(self, wheels=4, speed=80, power=90, random=True):
        super().__init__(wheels, speed, power, random)


class SportCars(Cars):
    def __init__(self, wheels=4, speed=300, power=500, random=True):
        super().__init__(wheels, speed, power, random)


class EstateCars(Cars):
    def __init__(self, wheels=4, speed=200, power=200, random=True):
        super().__init__(wheels, speed, power, random)


class MediumTrucks(Trucks):
    def __init__(self, wheels=6, speed=130, power=250, random=True):
        super().__init__(wheels, speed, power, random)


class HeavyTrucks(Trucks):
    def __init__(self, wheels=8, speed=111, power=800, random=True):
        super().__init__(wheels, speed, power, random)
