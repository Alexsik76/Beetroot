from vehicles2 import save_csv, class_cargo
from vehicles2.random_vehicles import matrix_objects
from vehicles2.routes import distance, get_route
from vehicles2.random_cargo import get_cargo

# path_st = 'standard_vehicles.csv'
# path = 'all_vehicles.csv'
# save_csv.get_standard_vehicles(path_st)
# data = save_csv.get_random_objects(path, 8)
# print(len(matrix_objects))
# cargo1 = class_cargo.Cargo(120, True, 2000, 1)
# # z = cargo1.dict_free[66].description
# # y = cargo1.dict_free[622].description
# for i in cargo1.sort_by_fuel():
#     print(f'{i.__class__.__name__:.<15}{i.speed:.<10}{i.fuel_costs}')
# print('='*40)
# for i in cargo1.sort_by_speed():
#     print(f'{i.__class__.__name__:.<15}{i.speed:.<10}{i.fuel_costs}')
r = get_route('Kalynivka', 'Chisinau')
d = distance('Kalynivka', 'Chisinau')
print('Route = ', r)
print('Distance = ', d)
cargo1 = class_cargo.Cargo('Kalynivka', 'Chisinau', 1000, 2000)
print(cargo1.distance)
cargo2 = get_cargo()
print(cargo2.a, cargo2.b, cargo2.distance, cargo2.payment, cargo2.capacity)
