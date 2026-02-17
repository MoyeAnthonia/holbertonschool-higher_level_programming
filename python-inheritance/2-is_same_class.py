#!/usr/bin/python3
"""exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Checks to see if the object is the same as the specified class"""
    return type(obj) is a_class
