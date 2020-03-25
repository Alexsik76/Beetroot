class Vehicles:
    def __init__(self, wheels, speed, power):
        self.wheels = wheels
        self.speed = speed
        self.power = power


class Bikes(Vehicles):
    def __init__(self):
        self.wheels = 2
        self.speed = 60
        self.power = 40


class Cars(Vehicles):
    def __init__(self):
        self.wheels = 4
        self.speed = 100
        self.power = 100


class Buses(Vehicles):
    def __init__(self):
        self.wheels = 4
        self.speed = 80
        self.power = 120


class Trucks(Vehicles):
    def __init__(self):
        self.wheels = 6
        self.speed = 100
        self.power = 200


class Pedal_bikes(Bikes):
    def __init__(self):
        self.speed = 40
        self.power = 0.5


class Motor_bikes(Bikes, Cars):
    def __init__(self):
        self.power = 60
        self.speed = 120


class Pick_ups(Cars):
    def __init__(self):
        self.power = 60
        self.speed = 80


class Sport_cars(Cars):
    def __init__(self):
        self.power = 500
        self.speed = 300


class Estate_cars(Cars):
    def __init__(self):
        self.power = 200
        self.speed = 220


class Medium_trucks(Trucks):
    def __init__(self):
        self.power = 600
        self.speed = 100


class Bikes1(Bikes):
    pass


class Heavy_trucks(Trucks):
    def __init__(self):
        self.power = 800
        self.speed = 120


b1 = Bikes1()
print(b1.power)
print(b1.speed)
print(b1.wheels)
