from random import randint
from vehicles2 import classes_of_cars
from vehicles2.random_param import get_param

matrix_objects = []


def get_random_class():
    k = randint(1, 7)
    if k == 1:
        return classes_of_cars.PedalBikes(*get_param('PedalBikes'))
    elif k == 2:
        return classes_of_cars.MotorBikes(*get_param('MotorBikes'))
    elif k == 3:
        return classes_of_cars.Minibus(*get_param('Minibus'))
    elif k == 4:
        return classes_of_cars.SportCars(*get_param('SportCars'))
    elif k == 5:
        return classes_of_cars.EstateCars(*get_param('EstateCars'))
    elif k == 6:
        return classes_of_cars.MediumTrucks(*get_param('MediumTrucks'))
    else:
        return classes_of_cars.HeavyTrucks(*get_param('HeavyTrucks'))
