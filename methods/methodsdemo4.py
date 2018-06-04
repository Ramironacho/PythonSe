"""
Variable Scope
"""

# a = 10
#
# def test_method(a):
#     print('Value of local a is: ' + str(a))
#     a = 2
#     print('New value of local a is: ' + str(a))
#
# print('Value of global a is: ' + str(a))
#
# test_method(a)
#
# print('Value of global a is: ' + str(a))

a = 10

def test_method():
    global a
    print('Value of a inside the method is: ' + str(a))
    a = 2
    print('New value of inside the method is: ' + str(a))

print('Value of global a is: ' + str(a))

test_method()

print('Value of global a is: ' + str(a))