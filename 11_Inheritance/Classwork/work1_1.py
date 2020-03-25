class Vehicles:
    def __init__(self, wheels=0, speed=0, power=0):
        self.wheels = wheels
        self.speed = speed
        self.power = power


class Bikes(Vehicles):
    def __init__(self, wheels=2, speed=40, power=20):
        self.wheels = wheels
        self.speed = speed
        self.power = power


class Pedal_bikes(Bikes):
    def __init__(self, wheels, speed, power):
        super().__init__(self, wheels)
        self.speed = 40
        self.power = 0.5


class Motor_bikes(Bikes):
    def __init__(self):
        self.power = 60
        self.speed = 120


v0 = Vehicles()
print(v0.wheels, v0.power, v0.speed)
b0 = Bikes()
print(b0.wheels, b0.power, b0.speed)
# b1 = Pedal_bikes()
# print(b1.power)
# print(b1.speed)
# print(b1.wheels)
