#!/usr/bin/env python3
"""CountedIterator class that counts iterated items"""


class Fish:
    """Iterator wrapper that counts fetched items"""

    def swim(self):
        """print(the iterator object itself"""
        print("The fish is swimming")

    def habitat(self):
        """print(next item and increment counter"""
        print("The fish lives in water")


class Bird:
    """Iterator wrapper that counts fetched items"""

    def fly(self):
        """print(the iterator object itself"""
        print("The bird is flying")

    def habitat(self):
        """print(next item and increment counter"""
        print("The bird lives in sky")


class FlyingFish(Fish, Bird):
    """inherited class"""

    def fly(self):
        """print(the iterator object itself"""
        print("The flying fish is soaring")

    def swim(self):
        """print(the iterator object itself"""
        print("The flying fish is swimming")

    def habitat(self):
        """print(the iterator object itself"""
        print("The flying fish lives in both water and the sky")
