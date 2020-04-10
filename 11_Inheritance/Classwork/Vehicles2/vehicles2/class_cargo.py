from vehicles2.random_vehicles import matrix_objects
from vehicles2.routes import distance


class Cargo:
    def __init__(self, city_a, city_b, payment, capacity):
        self.a = city_a
        self.b = city_b
        self.payment = payment
        self.capacity = capacity
        self.distance = distance(self.a, self.b)

    @property
    def free_vehicles(self):
        return list(filter(lambda x: not x.busy, matrix_objects))

    def sort_by_fuel(self):
        return sorted(self.free_vehicles, key=lambda x: (x.fuel_costs, x.speed))

    def sort_by_speed(self):
        return sorted(self.free_vehicles, key=lambda x: (x.speed, x.fuel_costs))
