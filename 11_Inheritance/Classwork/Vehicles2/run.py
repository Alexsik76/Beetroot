from vehicles2 import save_csv
from vehicles2.random_classes import matrix_objects

price_of_fuel = 25
path_st = 'standard_vehicles.csv'
path = 'all_vehicles.csv'
save_csv.get_standard_vehicles(path_st)
data = save_csv.get_random_objects(path, 130)
print(len(matrix_objects))
