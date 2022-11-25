# Encapsulation

class Employee:
    def __init__(self):
        # public properties
        self.name = "Ram Narayan"
        self.address = "Butwal"
        self.degicnation = "MD"

        # protected properties
        self._dob = '1997'
        self._emp_type = 'Full time'

        # private properties

        self.__email = 'rn@mycompany.com'
        self.__contact = '9800000000'

    def getuser_Email(self):
        print(f"Email: {self.__email}")

    def getuser_Contact(self):
        print(f"Contact: {self.__contact}")


emp = Employee()

print("----------\nPublic Properties")
emp.name = "Prakalpit Neupane"
emp.address = "Bardaghat"
emp.degicnation = "CEO"
print(emp.name)
print(emp.address)
print(emp.degicnation)

print("----------\nProtected Properties")
emp._dob = '1996-10-7'
emp._emp_type = "Full Time"
print(emp._dob)
print(emp._emp_type)

print("----------\nPrivate Properties")

emp.getuser_Email()
emp.getuser_Contact()


# accessing modifier  - accessing and storing values in private properties

class Person:
    def __init__(self):
        self.__gender = str
        self.__stage = str

    def getGender(self):
        return self.__gender

    def setGender(self, val):
        self.__gender = val

    def getStage(self):
        return self.__stage

    def setStage(self, val):
        self.__stage = val

    def getPersonDetails(self):
        print(self.getGender())
        print(self.getStage())


p1 = Person()

print("\n------Getter and setter-------")
p1.setGender("Male")
print(p1.getGender())
p1.setStage("Adult")
print(p1.getStage())
print('\n---------')
p1.getPersonDetails()
