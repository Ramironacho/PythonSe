"""
Object Oriented Programming
"""

class Car(object):

    def __init__(self, make, model= "550i"):
        self.make_car = make
        self.model_car = model

    def printMake(self):
        print(self.make_car)



c1 = Car("Fiat")


c2 = Car("bmw")
c1.printMake()
c2.printMake()
print(c2.model_car)