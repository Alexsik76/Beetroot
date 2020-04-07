import csv
from vehicles2.standard_classes import standard_data
from vehicles2.random_vehicles import get_random_class, matrix_objects


def csv_writer(func):
    """
    Write data to a CSV file path
    """
    def wrapper(path, *args):
        data = ["Class,wheels,speed,power,load capacity,capacity of people,fuel costs".split(",")]
        data.extend(func(*args))
        with open(path, "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for line1 in data:
                writer.writerow(line1)
        return data
    return wrapper


@csv_writer
def get_standard_vehicles():
    """
    Generates objects with standard characteristics that are specified in the file 'standard_classes.py'
    """
    data = []
    for key, value in standard_data.items():
        s = f"{key},{value['wheels']},{value['speed']},{value['power']}," \
            f"{value['load_capacity']},{value['capacity_of_people']},{value['fuel_costs']}"
        data.append(s.split(','))
    return data


@csv_writer
def get_random_objects(number: int):
    """
    Generates a {number} of objects with random characteristics
    """
    data = []
    for j in range(number):
        temp_object = get_random_class()
        matrix_objects.append(temp_object)
        line = temp_object.for_csv()
        data.append(line)
    return data
