#!/usr/bin/env python3
"""CountedIterator class that counts iterated items"""


class SwimMixin():
    """
    This is the SwimMixin class
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin():
    """
    This is the FlyMixin class
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    This is the Dragon class
    """
    def roar(self):
        print("The dragon roars!")
