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
