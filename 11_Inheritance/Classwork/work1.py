class Vehicles:
    def __init__(self, wheels, speed, power):
        self.wheels = wheels
        self.speed = speed
        self.power = power


class Bikes(Vehicles):
    def __init__(self):
        self.wheels = 2


class Cars(Vehicles):
    def __init__(self):
        self.wheels = 4


class Buses(Vehicles):
    def __init__(self):
        self.wheels = 4


class Trucks(Vehicles):
    def __init__(self):
        self.wheels = 6


class Pedal_bikes(Bikes):
    def __init__(self):
        self.power = 0.5


b1 = Pedal_bikes()
print(b1.power)
# b1.speed = 40
print(b1.speed)
