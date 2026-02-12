#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
     def test_max_integer(self):
          """Test empty list"""
          self.assertIsNone(max_integer([]))
    
     """Test one element in list"""
     def test_single(self):
        self.assertEqual(max_integer([5]), 5)

     """ Test Floats: both positive and negative"""
     def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 70.125, 3.456]), 70.125)
        self.assertEqual(max_integer([-1.45, 2.4, -6]), 2.4)
    
     """Test max element list"""
     def test_multiple(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

     """Test sprinkled Negative numbers"""
     def test_negative(self):
        self.assertEqual(max_integer([1, -2, 5, -6]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)


