#!/usr/bin/python3
"""adds two integers together"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a: First integer(int or float)
        b: Second integer (int or float)
    Return:
        the sum of a and b
    Raises:
        TypeError if a and b are not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a+b
