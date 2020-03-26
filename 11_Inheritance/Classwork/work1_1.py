class Vehicles:
    def __init__(self, wheels=0, speed=0, power=0):
        self.wheels = wheels
        self.speed = speed
        self.power = power


class Bikes(Vehicles):
    def __init__(self):
        super().__init__()
        self.wheels = 2


class Pedal_bikes(Bikes):
    def __init__(self):
        super().__init__()
        self.power = 0.5
        self.speed = 15


class Pedal_bikes_simple():
    def __init__(self, wheels=2, speed=11, power=0.7):
        self.wheels = wheels
        self.speed = speed
        self.power = power


pb = Pedal_bikes()
print(pb.wheels, pb.speed, pb.power)
pbs = Pedal_bikes_simple(power=100)
print(pbs.wheels, pbs.speed, pbs.power)
