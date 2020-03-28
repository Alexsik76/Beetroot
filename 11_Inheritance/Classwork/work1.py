import csv


class Vehicles:
    def __init__(self, wheels, speed, power):
        self.wheels = wheels
        self.speed = speed
        self.power = power

    @property
    def description(self):
        rez = f'\n{self.__class__.__name__}\nwheels: {self.wheels}\n speed: {self.speed}\n power: {self.power}\n'
        return rez


class Bikes(Vehicles):
    def __init__(self, wheels, speed, power):
        super().__init__(wheels, speed, power)


class Cars(Vehicles):
    def __init__(self, wheels, speed, power):
        super().__init__(wheels, speed, power)
        self.wheels = 4
        self.speed = 100
        self.power = 100


class Buses(Vehicles):
    def __init__(self, wheels, speed, power):
        super().__init__(wheels, speed, power)
        self.wheels = 4
        self.speed = 80
        self.power = 120


class Trucks(Vehicles):
    def __init__(self, wheels, speed, power):
        super().__init__(wheels, speed, power)
        self.wheels = 6
        self.speed = 100
        self.power = 200

# last Classes


class PedalBikes(Bikes):
    def __init__(self, wheels=2, speed=20, power=0.5):
        super().__init__(wheels, speed, power)


class MotorBikes(Bikes, Cars):
    def __init__(self, wheels=2, speed=180, power=200):
        super().__init__(wheels, speed, power)
        self.power = 60
        self.speed = 120


class PickUps(Cars):
    def __init__(self, wheels=4, speed=80, power=90):
        super().__init__(wheels, speed, power)


class SportCars(Cars):
    def __init__(self, wheels=4, speed=300, power=500):
        super().__init__(wheels, speed, power)
        self.power = 500
        self.speed = 300


class EstateCars(Cars):
    def __init__(self, wheels=4, speed=200, power=200):
        super().__init__(wheels, speed, power)
        self.power = 200
        self.speed = 220


class MediumTrucks(Trucks):
    def __init__(self, wheels=6, speed=130, power=250):
        super().__init__(wheels, speed, power)
        self.power = 600
        self.speed = 100


class HeavyTrucks(Trucks):
    def __init__(self, wheels=8, speed=100, power=1000):
        super().__init__(wheels, speed, power)
        self.power = 800
        self.speed = 120


b1 = PedalBikes()
print(b1.description)
ht1 = HeavyTrucks(8, 100, 900)
print(ht1.description)
print(dir(ht1))
print(PedalBikes().__class__.__name__)

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
        line=[]
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
