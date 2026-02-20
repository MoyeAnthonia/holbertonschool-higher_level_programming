#!/usr/bin/env python3
"""CountedIterator class that counts iterated items"""


class CountedIterator:
    """Iterator wrapper that counts fetched items"""

    def __init__(self, iterable):
        """Initialize with an iterable and counter"""
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        """Return the iterator object itself"""
        return self

    def __next__(self):
        """Return next item and increment counter"""
        item = next(self.iterator)  # May raise StopIteration
        self.counter += 1
        return item

    def get_count(self):
        """Return number of iterated items"""
        return self.counter
