from vehicles2.random_vehicles import matrix_objects
from vehicles2.dispatcher import dispatcher




def main_loop():
    for i in range(10_000):
        dispatcher()
        print('next hour')
        print('='*40)
        for vehicle in matrix_objects:
            if vehicle.cargo:
                if vehicle.speed >= vehicle.this_path_segment:
                    vehicle.kilometrage += vehicle.this_path_segment
                    vehicle.all_kilometrage += vehicle.this_path_segment
                    station = vehicle.route.pop(0)
                    if not vehicle.route:
                        vehicle.route = vehicle.get_new_route().copy()
                    vehicle.place = station
                    print(f'on station {station} arrived {vehicle.__class__.__name__}')
                    for cargo in vehicle.cargo:
                        if cargo.this_route[-1] == station:
                            cargo.route = list(set(cargo.route) - (set(cargo.this_route)))
                            if not cargo.route:
                                vehicle.money += cargo.payment
                                vehicle.cargo.remove(cargo)
                                print(f'Cargo weighing {cargo.capacity} delivered to {vehicle.place}.')
                else:
                    vehicle.kilometrage += vehicle.speed
                    vehicle.all_kilometrage += vehicle.speed
