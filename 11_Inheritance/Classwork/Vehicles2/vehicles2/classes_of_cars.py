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
        rez = f'\n{self.__class__.__name__}\n{"wheels":.<25}{self.wheels}\n{"speed:":.<25}{self.speed}' \
              f'\n{"power:":.<25}{self.power}\n{"load capacity:":.<25}{self.load_capacity}' \
              f'\n{"capacity of people:":.<25}{self.capacity_of_people}\n{"fuel costs:":.<25}{self.fuel_costs}'
        return rez

    def for_csv(self):
        rez = [
            self.__class__.__name__,
            self.wheels,
            self.speed,
            self.power,
            self.load_capacity,
            self.capacity_of_people,
            self.fuel_costs
        ]
        return rez


class Bikes(Vehicles):
    def __init__(self, wheels, speed, power, load_capacity, capacity_of_people, fuel_costs):
        super().__init__(wheels, speed, power, load_capacity, capacity_of_people, fuel_costs)


class Cars(Vehicles):
    def __init__(self, wheels, speed, power, load_capacity, capacity_of_people, fuel_costs):
        super().__init__(wheels, speed, power, load_capacity, capacity_of_people, fuel_costs)


class Buses(Vehicles):
    def __init__(self, wheels, speed, power, load_capacity, capacity_of_people, fuel_costs):
        super().__init__(wheels, speed, power, load_capacity, capacity_of_people, fuel_costs)


class Trucks(Vehicles):
    def __init__(self, wheels, speed, power, load_capacity, capacity_of_people, fuel_costs):
        super().__init__(wheels, speed, power, load_capacity, capacity_of_people, fuel_costs)


# last Classes


class PedalBikes(Bikes):
    def __init__(self, wheels, power, speed, load_capacity, capacity_of_people, fuel_costs):
        super().__init__(wheels, power, speed, load_capacity, capacity_of_people, fuel_costs)


class MotorBikes(Bikes, Cars):
    def __init__(self, wheels, power, speed, load_capacity, capacity_of_people, fuel_costs):
        super().__init__(wheels, power, speed, load_capacity, capacity_of_people, fuel_costs)


class Minibus(Buses):
    def __init__(self, wheels, power, speed, load_capacity, capacity_of_people, fuel_costs):
        super().__init__(wheels, power, speed, load_capacity, capacity_of_people, fuel_costs)


class SportCars(Cars):
    def __init__(self, wheels, power, speed, load_capacity, capacity_of_people, fuel_costs):
        super().__init__(wheels, speed, power, load_capacity, capacity_of_people, fuel_costs)


class EstateCars(Cars):
    def __init__(self, wheels, power, speed, load_capacity, capacity_of_people, fuel_costs):
        super().__init__(wheels, speed, power, load_capacity, capacity_of_people, fuel_costs)


class MediumTrucks(Trucks):
    def __init__(self, wheels, power, speed, load_capacity, capacity_of_people, fuel_costs):
        super().__init__(wheels, speed, power, load_capacity, capacity_of_people, fuel_costs)


class HeavyTrucks(Trucks):
    def __init__(self, wheels, power, speed, load_capacity, capacity_of_people, fuel_costs):
        super().__init__(wheels, speed, power, load_capacity, capacity_of_people, fuel_costs)
