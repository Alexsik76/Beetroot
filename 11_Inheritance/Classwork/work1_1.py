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


pb = Pedal_bikes()
print(pb.wheels, pb.speed, pb.power)
# b1 = Pedal_bikes()
# print(b1.power)
# print(b1.speed)
# print(b1.wheels)
