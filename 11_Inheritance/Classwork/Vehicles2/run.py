from vehicles2 import save_csv, class_cargo
from vehicles2.random_vehicles import matrix_objects

price_of_fuel = 25
path_st = 'standard_vehicles.csv'
path = 'all_vehicles.csv'
save_csv.get_standard_vehicles(path_st)
data = save_csv.get_random_objects(path, 800)
print(len(matrix_objects))
cargo1 = class_cargo.Cargo(120, True, 2000, 1)
z = cargo1.dict_free.get(66).description
y = cargo1.dict_free.get(622).description
print(z, y)
