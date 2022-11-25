# Example
class Bike():
    # below are the attributes
    # <attributes> = <value>
    chasis = "Triangular Shape"
    engine = "1200 CC"
    handle = "Large"
    wheel = "Alloy"
    Tyre = "Tubeless"
    headlight = "LED"
    seat = "Premium Leather"
    mirror = "High Quality"

# Methods

    def BreakingSystem(self):
        print("This is the Breaking System")

    def EngineDetails(self):
        print("Engine Details")

    #accessing class properties/attributes via class name

print(Bike.chasis)
print(Bike.engine)
print(Bike.seat)


# accessing class properties and attributes by creating objects
print("-------------By Creating Objects-------------")
Pulsar = Bike()
print("Chasis: ", Pulsar.chasis)

# accessing class names via objects
print("-------------Methods-------------")
Avenger = Bike()
print(Avenger.chasis)
print("--Calling Methods--")
Avenger.EngineDetails()
Avenger.BreakingSystem()

print("-------------ID-------------")
print(id(Avenger))
print(id(Pulsar))

print("------------- Storing Attributes via obj ------------- ")
# set custom engine size for the programme
Pulsar.engine = "220 CC"
Avenger.engine = "800 CC"
# modify the chasis
Pulsar.chasis = "Muscular"
Avenger.chasis = "Rectangular"

print(Pulsar.engine)
print(Pulsar.chasis)
print(Avenger.engine)
print(Avenger.chasis)