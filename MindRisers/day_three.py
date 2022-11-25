#inheritance
class Vehicle():
    def __init__(self):
        self.brand = "Tesla"
        self.engine = "Battery Based"
        self.price = "2M"

    def getVehicleDetails(self):
        print(self.brand)
        print(self.engine)
        print(self.price)


class TeslaModelX(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.model = "TeslaX"
        self.mode = "Automatic"

    def getTeslaModelXDetails(self):
        print("Brand: ", self.brand)
        print("Price: ", self.price)
        print("Model: ", self.model)
        print("Mode: ", self.mode)

c1 = TeslaModelX()
c1.getTeslaModelXDetails()
print("-----")
c1.getVehicleDetails()

#### Example Two
class Mobile():
    def __init__(self):
        self.brand = "MI"
        self.madeIn = "China"
        self.price = "32K"

    def getMobileInfo(self):
        print(self.brand)
        print(self.madeIn)
        print(self.price)

class NodeE(Mobile):
    def __init__(self):
        super().__init__()
        self.range = "Top End"
        self.name = "NodeE"

    def getNodeEDetails(self):
        print(self.range)
        print(self.name)

print("======")
m1 = NodeE()
m1.getMobileInfo()
print("-----")
m1.getNodeEDetails()


# Above examples were single Inheritance

# Example 3 - Multiple Inheritance

class Shape():
    def show(self):
        print("This is a Shape")

class Area():
    def showArea(self):
        print("This is Area")

class Quadilateral():
    def showDetails(self):
        print("This has 4 sides")

class Perimeter():
    def showPerimeteR(self):
        print("This is a perimeter")


class Square(Shape,Quadilateral,Area,Perimeter):
    def showSquare(self):
        print("This is a Square")


shape_1 = Square()
print("\nMultiple Inheritance\n")
shape_1.show()
shape_1.showSquare()
shape_1.showArea()
shape_1.showPerimeteR()

# Multi-Level Inheritance
print("\n------ Multi-Level Inheritance -------\n")
class GrandFather():
    def showGrandFather(self):
        print("I am a GrandFather")

class Father(GrandFather):
    def showFather(self):
        print("I am a Father\n")
        self.showGrandFather()

class Son(Father):
    def showSon(self):
        print("I am a son!!\n")
        self.showFather()
        self.showGrandFather()

s1 = Son()
s1.showSon()

# parameterized constructor Example

class Sum():
    def __init__(self, num_1, num_2):
        self.one = num_1
        self.two = num_2

    def sumOF(self):
        return self.one + self.two

class Product():
    def __init__(self, num_1, num_2):
        self.one = num_1
        self.two = num_2

    def productOF(self):
        return self.one * self.two


class Calculator(Sum, Product):
    def __init__(self, num_1, num_2):
        Sum.__init__(self, num_1, num_2)
        Product.__init__(self, num_1, num_2)
        self.totalSum = 0.00
        self.totalProduct = 0.00

    def CalculateSum(self):
        self.totalSum = self.sumOF()
        print("Sum of two numbers: ", self.totalSum)

    def CalculateProduct(self):
        self.totalProduct = self.productOF()
        print("Product of two numbers: ", self.totalProduct)


print("\nModern OOP Calculator\n")
c1 = Calculator(12,5)
c1.CalculateSum()
c1.CalculateProduct()



