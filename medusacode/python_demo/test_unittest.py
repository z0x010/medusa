#!/usr/bin/env python
# coding:utf-8

"""
Python unittest
"""

import unittest

def func(a, b):
    return a + b

class TestFunc(unittest.TestCase):
    """
    unittest
    """
    def test_int(self):
        self.assertEqual(func(1, 2), 3)

    def test_float(self):
        self.assertEqual(func(1.0, 2.0), 3.0)

    def test_str(self):
        self.assertEqual(func('a', 'b'), 'ab')

if __name__ == '__main__':
    unittest.main()
