import csv


def csv_dict_reader(path):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(path, delimiter=',')
    obj = []
    for line in reader:
        obj0 = [line['wheels'], line['speed'], line['power']]
        obj.append(list(map(int, obj0)))
    return obj

def read(path):
    with open(path) as f_obj:
     return csv_dict_reader(f_obj)
