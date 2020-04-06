from random import randint
from vehicles import classes_of_cars


def generate():

    def random_class():
        k = randint(1, 7)
        if k == 1:
            return classes_of_cars.PedalBikes()
        elif k == 2:
            return classes_of_cars.MotorBikes()
        elif k == 3:
            return classes_of_cars.PickUps()
        elif k == 4:
            return classes_of_cars.SportCars()
        elif k == 5:
            return classes_of_cars.EstateCars()
        elif k == 6:
            return classes_of_cars.MediumTrucks()
        else:
            return classes_of_cars.HeavyTrucks()

    data = ["Class,wheels,speed,power".split(",")]
    lists_of_objects = []

    for j in range(1000):
        temp_object = random_class()
        lists_of_objects.append(temp_object)
        line = temp_object.for_csv()
        data.append(line)

    return data
