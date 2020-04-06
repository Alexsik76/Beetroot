import csv


def csv_dict_reader(path):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(path, delimiter=',')
    obj = []
    for line in reader:
        obj0 = [line['name'],
                int(line['wheels']),
                int(line['speed']),
                int(line['power']),
                int(line['load_capacity']),
                int(line['capacity_of_people']),
                float(line['fuel_costs'])
                ]
        obj.append(obj0)

    return obj

def read(path):
    with open(path) as f_obj:
        return csv_dict_reader(f_obj)
