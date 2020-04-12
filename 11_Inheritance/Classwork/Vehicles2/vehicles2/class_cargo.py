from vehicles2.random_vehicles import matrix_objects
from vehicles2.routes import distance, get_route


class Cargo:
    def __init__(self, city_a, city_b, payment, capacity):
        self.a = city_a
        self.b = city_b
        self.route = get_route(self.a, self.b)
        self.distance = distance(self.a, self.b)
        self.payment = payment
        self.capacity = capacity
        self.this_route = self.route

    @property
    def description(self):
        rez = f'\nCargo\n{"a:":.<25}{self.a}' \
              f'\n{"b:":.<25}{self.b}\n{"capacity:":.<25}{self.capacity}' \
              f'\n route: {self.route}\n this_route: {self.this_route}'
        return rez

    # @property
    # def free_vehicles(self):
    #     return list(filter(lambda x: not x.busy, matrix_objects))
    #
    #
    #
    # def sort_by_fuel(self):
    #     return sorted(self.free_vehicles, key=lambda x: (x.fuel_costs, x.speed))
    #
    # def sort_by_speed(self):
    #     return sorted(self.free_vehicles, key=lambda x: (x.speed, x.fuel_costs))
