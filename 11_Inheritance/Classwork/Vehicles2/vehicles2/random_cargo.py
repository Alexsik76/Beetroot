from random import randint
from vehicles2.class_cargo import Cargo
from vehicles2.routes import distances, distance


def get_cargo():
    city_list = list(distances.keys())
    city_a = city_list.pop(randint(0, len(city_list) - 1))
    city_b = city_list[randint(0, len(city_list) - 1)]
    capacity = randint(10, 2000)
    dist = distance(city_a, city_b)
    payment = round((dist * capacity * 0.008), 2)
    return Cargo(city_a, city_b, payment, capacity)
