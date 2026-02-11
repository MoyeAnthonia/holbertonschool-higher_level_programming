#!/usr/bin/python3
"""
This module contains a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers together.

    Args:
        a: First number (must be int or float)
        b: Second number (must be int or float), defaults to 98

    Returns:
        The sum of a and b as an integer

    Raises:
        TypeError: If a or b is not an integer or float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
