from vehicles2.random_cargo import get_cargo
from vehicles2.random_vehicles import matrix_objects
from vehicles2.classes_of_cars import Vehicles

list_of_cargo = []


def dispatcher():
    while len(list_of_cargo) < 100:
        list_of_cargo.append(get_cargo())

    def free_vehicles():
        return list(filter(lambda x: not x.busy, matrix_objects))

    def find_vehicle(cargo):
        for vehicle in free_vehicles():
            if vehicle.free_capacity >= cargo.capacity and len(vehicle.route) > 1:
                a = cargo.route[0]
                a1 = cargo.route[1]
                if a in vehicle.route and \
                        a1 in vehicle.route and \
                        vehicle.route.index(a1) > vehicle.route.index(a):
                    assert isinstance(vehicle, Vehicles)
                    return vehicle

    def to_give_cargo():
        for cargo in list_of_cargo:
            vehicle = find_vehicle(cargo)
            if vehicle:
                vehicle.cargo.append(cargo)
                list_of_cargo.remove(cargo)
