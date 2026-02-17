#!/usr/bin/python3
"""a base class that inherits from super class"""


class MyList(list):
    """atrributes are not needed"""

    def print_sorted(self):
        """Docstring for print_sorted
        :param self: Description
        """
        print(sorted(self))
