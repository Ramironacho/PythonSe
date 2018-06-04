"""
Object Oriented Programming
"""

class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make_car = make
        self.model_car = model

    def printMake(self):
        print(self.make_car)

    def info(self):
        print("Make of the car: " + self.make_car)
        print("Model of the car: " + self.model_car)



c1 = Car("bmw", "550i")
c1.wheels = 3
c2 = Car("benz", "E350")
c1.info()
print(c1.wheels)
c2.info()
print(c2.wheels)
print(Car.wheels)