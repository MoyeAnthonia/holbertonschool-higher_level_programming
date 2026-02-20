#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""Creating an abstract class"""


class VerboseList (list):
    def append(self, item):
        """Empty sound method"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        """call the parent method"""
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")

    def remove(self, item):
        """call the parent method"""
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, item):
        """call the parent method"""
        super().pop(item)
        print(f"Popped [{item}] from the list.")
