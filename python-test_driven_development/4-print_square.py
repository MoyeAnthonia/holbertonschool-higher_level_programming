#!/usr/bin/python3
"""
This module contains a function that prints a square with the character #
"""


def print_square(size):
    """
    Docstring for print_square

    Args:
    :param size: Integer (size must be an integer)

    Returns:
    size

    Raises:
    TypeError: If size is not integer

    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if isinstance(size, int) and size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    size = int(size)
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
