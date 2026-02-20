#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""Creating an abstract class"""


class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Empty sound method"""
        pass

class Dog(Animal):
    def sound(self):
        """call the parent method"""
        return "Bark"

class Cat(Animal):
    def sound(self):
        """call the parent method"""
        return "Meow"
