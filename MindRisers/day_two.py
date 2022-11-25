print("\n===== non-parametrized constructor =====\n")


class Shoes():
    # non-parametrized constructor
    def __init__(self):
        self.brand = "GoldStar"
        self.model = "Classic"
        self.price = "850"
        self.madeIn = "Nepal"

    def getDetails(self):
        print("model: ", self.model)
        print("price: ", self.price)


'''
Above is the example of non parametrized constructor
'''
g1 = Shoes()
g1.getDetails()

# parametrized constructor
print("\n==== parametrized constructor ====\n")


class MobilePhone():
    def __init__(self, parm_brand, parm_model, parm_range, parm_price):
        self.brand = parm_brand
        self.model = parm_model
        self.range = parm_range
        self.price = parm_price

    def getCellInfo(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("range: ", self.range)
        print("price: ", self.price)


# now we will pass the arguments here itself as the constructor is parametrized
m1 = MobilePhone("Apple", "Iphone 13", "Top End", "1,30,000")
m1.getCellInfo()
