from vehicles2.random_cargo import get_cargo
from vehicles2.random_vehicles import matrix_objects
from vehicles2.classes_of_cars import Vehicles
from vehicles2.class_cargo import Cargo

list_of_cargo = []

def dispatcher():
    while len(list_of_cargo) < 100:
        list_of_cargo.append(get_cargo())

    def free_vehicles():
        rez = list(filter(lambda x: not x.busy, matrix_objects))
        return rez

    def find_vehicle(cargo):
        list_free_vehicles = free_vehicles()
        for vehicle in list_free_vehicles:
            if (vehicle.free_capacity >= cargo.capacity) and (len(vehicle.route) > 1):
                if cargo.route[0] in vehicle.route and \
                        cargo.route[1] == vehicle.route[1]:
                    assert isinstance(vehicle, Vehicles)
                    return vehicle
            elif (vehicle.free_capacity >= cargo.capacity) and (len(vehicle.route) == 0):
                if vehicle.place == cargo.route[0]:
                    return vehicle
    def to_give_cargo():
        for cargo in list_of_cargo:
            vehicle = find_vehicle(cargo)
            if vehicle:
                vehicle.cargo.append(cargo)
                print(f'{vehicle.__class__.__name__} to give {cargo.capacity} in {cargo.a}')
                if len(cargo.route) > len(vehicle.route):
                    vehicle.route = cargo.route.copy()
                    cargo.this_route = list(set(vehicle.route) & set(cargo.route))
                list_of_cargo.remove(cargo)

    def run_vehicles():
        list_min_cargo = sorted(list_of_cargo, key=lambda x: x.capacity)
        min_cargo = list_min_cargo[0]
        for vehicle in matrix_objects:
            assert isinstance(min_cargo, Cargo)
            if vehicle.free_capacity < min_cargo.capacity:
                vehicle.busy = True

    to_give_cargo()

    run_vehicles()
