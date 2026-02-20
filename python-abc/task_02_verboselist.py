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
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"Item [{item}] not found in the list.")

    def pop(self, item=-1):
        """call the parent method"""
        print(f"Popped [{self[item]}] from the list.")
        super().pop(item)
