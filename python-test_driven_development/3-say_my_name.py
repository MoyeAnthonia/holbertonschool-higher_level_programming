#!/usr/bin/python3
"""
This module contains a function that prints out name.
"""


def say_my_name(first_name, last_name=""):
    """
    Docstring for say_my_name

    Args:
    :param first_name: String (must be a string)
    :param last_name: String (must be a string)

    Returns:
    a first_name and last_name

    Raises:
    TypeError: If first_name is not string
    TypeError: If last_name is not string

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")

    return
