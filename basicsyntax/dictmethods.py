car = {'make': 'bmw', 'model': '550i', 'year': 2016}
cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}

print(car.keys())
print(cars.keys())
print(car.values())
print(cars.values())
print(car.items())

car_copy = car.copy()
print(car_copy)

print(car.pop('model'))
print(car)

car.clear()
print(car)


d={"key1": [1, 2, 3], "key2": [4, 5, 6], "key3": [7, 8, 9]}

print(d["key3"][0])