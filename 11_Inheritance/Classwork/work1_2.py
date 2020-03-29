import csv
from random import randint


def random_value(value):
    return randint((value - int(value/10)), (value + int(value/10)))


class Vehicles:
    min_sp = None
    max_sp = None
    min_pow = None
    max_pow = None

    def __init__(self, wheels, speed, power, random=True):
        self.random = random
        self.wheels = wheels
        self.speed = speed
        self.power = power
        self.speed_power(self.random)

    def speed_power(self, random):
        if random:
            self.speed = random_value(self.speed)
            self.power = random_value(self.power)
            print(self.speed)
        else:
            self.speed = self.speed
            self.power = self.power
            print(self.speed)
    @property
    def description(self):
        rez = f'\n{self.__class__.__name__}\nwheels: {self.wheels}\n speed: {self.speed}\n power: {self.power}\n'
        return rez

    def intervals(self):
        i_sp = int(self.speed / 10)
        i_pow = int(self.power / 10)
        self.min_sp = self.speed - i_sp
        self.max_sp = self.speed + i_sp
        self.min_pow = self.speed - i_pow
        self.max_pow = self.speed + i_pow

    def comparison(self, obj):
        self.intervals()
        if (obj[0] == self.wheels
                and self.min_sp <= obj[1] <= self.max_sp
                and self.min_pow <= obj[1] <= self.max_pow):
            print(f'{self.min_sp} , {obj[1]} , {self.max_sp}')
            return True


class Bikes(Vehicles):
    def __init__(self, wheels, speed, power, random=True):
        super().__init__(wheels, speed, power, random)


class Cars(Vehicles):
    def __init__(self, wheels, speed, power, random=True):
        super().__init__(wheels, speed, power, random)


class Buses(Vehicles):
    def __init__(self, wheels, speed, power, random=True):
        super().__init__(wheels, speed, power, random)


class Trucks(Vehicles):
    def __init__(self, wheels, speed, power, random=True):
        super().__init__(wheels, speed, power, random)


# last Classes


class PedalBikes(Bikes):
    def __init__(self, wheels=2, speed=20, power=15, random=True):
        super().__init__(wheels, speed, power, random)


class MotorBikes(Bikes, Cars):
    def __init__(self, wheels=2, speed=180, power=200, random=True):
        super().__init__(wheels, speed, power, random)


class PickUps(Cars):
    def __init__(self, wheels=4, speed=80, power=90, random=True):
        super().__init__(wheels, speed, power, random)


class SportCars(Cars):
    def __init__(self, wheels=4, speed=300, power=500, random=True):
        super().__init__(wheels, speed, power, random)


class EstateCars(Cars):
    def __init__(self, wheels=4, speed=200, power=200, random=True):
        super().__init__(wheels, speed, power, random)


class MediumTrucks(Trucks):
    def __init__(self, wheels=6, speed=130, power=250, random=True):
        super().__init__(wheels, speed, power, random)


class HeavyTrucks(Trucks):
    def __init__(self, wheels=8, speed=111, power=800, random=True):
        super().__init__(wheels, speed, power, random)


h = PedalBikes(random=True)
print(h.description)
list_of_classes = [PedalBikes(),
                   MotorBikes(),
                   PickUps(),
                   SportCars(),
                   EstateCars(),
                   MediumTrucks(),
                   HeavyTrucks()]
lists_of_objects = {'PedalBikes': [],
                    'MotorBikes': [],
                    'PickUps': [],
                    'SportCars': [],
                    'EstateCars': [],
                    'MediumTrucks': [],
                    'HeavyTrucks': []
                    }
k = 0
data = ["Class,Number,wheels,speed,power".split(",")]
for z, i in lists_of_objects.items():
    for j in range(10):
        i.append(list_of_classes[k])
        print(z, j)
        line = []
        line.append(z)
        line.append(j)
        line.append(i[j].wheels)
        line.append(i[j].speed)
        line.append(i[j].power)
        data.append(line)
        print(f'{i[j].description}')
    k += 1


def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line1 in data:
            writer.writerow(line1)


path = "vehicles.csv"

csv_writer(data, path)


def statistic(path):
    list_of_founded = {
        'IN ALL':       0,
        'PedalBikes':   0,
        'MotorBikes':   0,
        'PickUps':      0,
        'SportCars':    0,
        'EstateCars':   0,
        'MediumTrucks': 0,
        'HeavyTrucks':  0
    }

    def csv_dict_reader(path):
        """
        Read a CSV file using csv.DictReader
        """
        reader = csv.DictReader(path, delimiter=',')
        for line in reader:
            for item in list_of_classes:
                temp = item
                # print(type(line), line)
                obj0 = [line['wheels'], line['speed'], line['power']]
                obj = list(map(int, obj0))
                if temp.comparison(obj):
                    list_of_founded['IN ALL'] += 1
                    list_of_founded[temp.__class__.__name__] += 1

    with open(path) as f_obj:
        csv_dict_reader(f_obj)

    for key, value in list_of_founded.items():
        print(f'{key:13}: {value}')


statistic(path)
