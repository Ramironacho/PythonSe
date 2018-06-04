"""
Positional Parameters
They are like optional parameters
And can be assigned a default value, if no value is provided from outside
"""


def sum_nums(n1, n2=5):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


sum1 = sum_nums(4)
print(sum1)
sum2 = sum_nums(n2=12, n1=5)
print(sum2)