from random import randint
from vehicles2.routes import distance


def random_value(value):
    return randint((value - int(value / 10)), (value + int(value / 10)))


class Vehicles:
    price_of_fuel = 25

    def __init__(self, wheels, speed, power, load_capacity, fuel_costs):
        self.wheels = wheels
        self.speed = speed
        self.power = power
        self.load_capacity = load_capacity
        self.fuel_costs = fuel_costs
        self.price_of_fuel = 25
        self.cargo = []
        self.busy = self.is_busy()
        self.route = []
        self.cost_of_transportation = self.cost
        self.free_capacity = self.get_free_capacity
        self.kilometrage = 0
        self.all_kilometrage = 0
        self.cargo_finished = []
        self.this_path_segment = self.get_this_path_segment
        self.place = 'Vinnytsia'
        self.money = 0

    @property
    def description(self):
        rez = f'\n{self.__class__.__name__}\n{"speed:":.<25}{self.speed}' \
              f'\n{"power:":.<25}{self.power}\n{"load capacity:":.<25}{self.load_capacity}' \
              f'\n{"fuel costs:":.<25}{self.fuel_costs}\n{"busy:":.<25}{self.busy}\n{self.route}\n{self.cargo}' \
              f'\n{"money:":.<25} {self.money}\n{"place:":.<25} {self.place} '
        return rez

    @property
    def cost(self):
        if self.cargo and self.route:
            dist_forward = distance(self.route[0], self.route[-1])
            dist_back = distance(self.route[-1], 'Vinnytsia')
            return sum([x.payment for x in self.cargo]) - ((dist_forward + dist_back) * self.price_of_fuel)
        else:
            return None

    @property
    def get_free_capacity(self) -> int:
        free = self.load_capacity - sum([x.capacity for x in self.cargo])
        return free

    @property
    def get_this_path_segment(self) -> int:
        if len(self.route) >= 2:
            return distance(self.route[0], self.route[1])
        else:
            return 0

    def is_busy(self):
        if not self.cargo:
            return False
        else:
            return True

    def get_new_route(self):
        if self.cargo:
            rez = sorted(self.cargo, key=lambda x: -len(x.route))
            return rez[0].route

    def for_csv(self):
        rez = [
            self.__class__.__name__,
            self.speed,
            self.power,
            self.load_capacity,
            self.fuel_costs
        ]
        return rez


class Cars(Vehicles):
    def __init__(self, wheels, speed, power, load_capacity, fuel_costs):
        super().__init__(wheels, speed, power, load_capacity, fuel_costs)


class Buses(Vehicles):
    def __init__(self, wheels, speed, power, load_capacity, fuel_costs):
        super().__init__(wheels, speed, power, load_capacity, fuel_costs)


class Trucks(Vehicles):
    def __init__(self, wheels, speed, power, load_capacity, fuel_costs):
        super().__init__(wheels, speed, power, load_capacity, fuel_costs)


# last Classes

class Minibus(Buses):
    def __init__(self, wheels, power, speed, load_capacity, fuel_costs):
        super().__init__(wheels, power, speed, load_capacity, fuel_costs)


class MediumTrucks(Trucks):
    def __init__(self, wheels, power, speed, load_capacity, fuel_costs):
        super().__init__(wheels, speed, power, load_capacity, fuel_costs)


class HeavyTrucks(Trucks):
    def __init__(self, wheels, power, speed, load_capacity, fuel_costs):
        super().__init__(wheels, speed, power, load_capacity, fuel_costs)
