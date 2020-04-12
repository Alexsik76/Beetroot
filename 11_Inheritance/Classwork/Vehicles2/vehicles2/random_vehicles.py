from random import randint
from vehicles2 import classes_of_cars
from vehicles2.random_param import get_param

matrix_objects = []


def get_random_class():
    k = randint(1, 3)
    if k == 1:
        return classes_of_cars.Minibus(*get_param('Minibus'))
    elif k == 2:
        return classes_of_cars.MediumTrucks(*get_param('MediumTrucks'))
    else:
        return classes_of_cars.HeavyTrucks(*get_param('HeavyTrucks'))
