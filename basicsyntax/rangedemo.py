"""
Built-in function
Creates a sequence of numbers but does not save them in memory
Very useful for generating numbers
"""

print(list(range(0, 10)))

a = range(0, 10)
print(a)
print(type(a))

print(list(a))

b = range(0, 10, 2)

print(list(b))
l = [1, 2, 3]
for num in range(3):
    print(num)