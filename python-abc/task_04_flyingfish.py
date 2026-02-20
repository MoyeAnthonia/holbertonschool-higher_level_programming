#!/usr/bin/env python3
"""CountedIterator class that counts iterated items"""


class Fish():
    """
    This is the Fish class
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird():
    """
    This is the Bird class
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Bird, Fish):
    """
    This is the FlyingFish class

    Inherits: Bird and Fish
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")