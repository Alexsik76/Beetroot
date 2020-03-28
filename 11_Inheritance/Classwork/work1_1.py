class Vehicles:
    def __init__(self, wheels=0, speed=0, power=0):
        self.wheels = wheels
        self.speed = speed
        self.power = power


class Bikes(Vehicles):
    def __init__(self):
        super().__init__()
        self.wheels = 2


class PedalBikes(Bikes):
    def __init__(self):
        super().__init__()
        self.power = 0.5
        self.speed = 15


class PedalBikesSimple:
    def __init__(self, wheels=2, speed=11, power=0.7):
        self.wheels = wheels
        self.speed = speed
        self.power = power


pb = PedalBikes()
print(pb.wheels, pb.speed, pb.power)
pbs = PedalBikesSimple(power=100)
print(pbs.wheels, pbs.speed, pbs.power)
