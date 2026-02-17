#!/usr/bin/python3
"""exactly an instance of the specified class"""


def inherits_from(obj, a_class):
    """returns true if the object's class matches the search case"""
    return issubclass(obj.__class__, a_class) and obj.__class__ is not a_class
