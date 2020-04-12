from vehicles2 import save_csv, class_cargo
from vehicles2.random_vehicles import matrix_objects
from vehicles2.routes import distance, get_route
from vehicles2.random_cargo import get_cargo
from vehicles2.main_loop import main_loop

money = 0
path_st = 'standard_vehicles.csv'
path = 'all_vehicles.csv'
save_csv.get_standard_vehicles(path_st)
data = save_csv.get_random_objects(path, 5)
print('Matrix_objects:', len(matrix_objects))
main_loop()
print('*'* 40)
for vehicle in matrix_objects:
    print(vehicle.description)