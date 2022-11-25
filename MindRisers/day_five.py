# polymorphism

class Vehicle:
    def __init__(self):
        self.vehicle_type = str
        self.brand = str
        self.category = str

    def brake(self):
        print("The Vehicle will stop")


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.brand = "Lamborghini"
        self.vehicle_type = "Four Wheel"
        self.category = "Super Car"

    def brake(self):
        print("Breaking system in car is different")
        print("System Mechanism is also different")


class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self.brand = "Kawasaki"
        self.category = "Super Bike"
        self.vehicle_type = "Two Wheeler"

    def brake(self):
        print("The biking system in bike is different")


b1 = Bike()
b1.brake()

c1 = Car()
c1.brake()
