from vehicles2.random_vehicles import matrix_objects


class Cargo:
    def __init__(self, distance, capacity=None, number_of_peoples=None, is_urgent=False, ):
        self.distance = distance
        self.is_urgent = is_urgent
        self.capacity = capacity
        self.number_of_peoples = number_of_peoples

    @property
    def free_vehicles(self):
        return list(filter(lambda x: not x.busy, matrix_objects))

    def sort_by_fuel(self):
        return sorted(self.free_vehicles, key = lambda x: (x.fuel_costs, x.speed))

    def sort_by_speed(self):
        return sorted(self.free_vehicles, key = lambda x: (x.speed, x.fuel_costs))
