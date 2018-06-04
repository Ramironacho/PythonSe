class Fruit(object):
    def __init__(self):
        print("New fruit created!")

    def nutrition(self):
        print("Nutritional value")

    def fruit_shape(self):
        print("Shape of the Fruit")

class Banana(Fruit):
    def __init__(self):
        super(Banana, self).__init__()
        print("New Banana")

    def nutrition(self):
        print("Nutritional value of Banana is: 125")

    def color(self):
        print("Color of Banana is yellow")


fruit = Fruit()
fruit.nutrition()
fruit.fruit_shape()

print("*"*50)


banana = Banana()
banana.fruit_shape()
banana.color()
banana.nutrition()
