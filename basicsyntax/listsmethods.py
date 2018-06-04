cars = ["bmw", "honda", "audi"]
s= cars.count("honda")
print(s)
length = len(cars)
print(length)

cars.append("benz")
print(cars)

cars.insert(1, "jeep")
print(cars)

x = cars.index("honda")
print (x)

y = cars.pop()
print(y)
print(cars)

cars.remove("jeep")
print(cars)
print(len(cars))
slicing = cars[0:2]
a = cars[1:len(cars)]
print(slicing)
print(a)
cars.sort()
print(cars)