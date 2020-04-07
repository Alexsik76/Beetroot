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

    # todo create dict of free_vehicles
    @property
    def dict_free(self):
        numbers = list(range(len(self.free_vehicles)))
        dict_to_sort = dict.fromkeys(numbers)
        for i in numbers:
            dict_to_sort[i] = self.free_vehicles[i]
        return dict_to_sort
