class Vehicles:
    def __init__(self, wheels, speed, power):
        self.wheels = wheels
        self.speed = speed
        self.power = power


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


class PedalBikes(Bikes):
    def __init__(self, wheels=2, speed=20, power=0.5):
        super().__init__(wheels, speed, power)


class MotorBikes(Bikes, Cars):
    def __init__(self, wheels, speed, power):
        super().__init__(wheels, speed, power)
        self.power = 60
        self.speed = 120


class PickUps(Cars):
    def __init__(self, wheels, speed, power):
        super().__init__(wheels, speed, power)


class SportCars(Cars):
    def __init__(self, wheels, speed, power):
        super().__init__(wheels, speed, power)
        self.power = 500
        self.speed = 300


class EstateCars(Cars):
    def __init__(self, wheels, speed, power):
        super().__init__(wheels, speed, power)
        self.power = 200
        self.speed = 220


class MediumTrucks(Trucks):
    def __init__(self, wheels, speed, power):
        super().__init__(wheels, speed, power)
        self.power = 600
        self.speed = 100


class HeavyTrucks(Trucks):
    def __init__(self, wheels, speed, power):
        super().__init__(wheels, speed, power)
        self.power = 800
        self.speed = 120


b1 = PedalBikes()
print(b1.power)
print(b1.speed)
print(b1.wheels)
