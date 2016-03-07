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
    A testcase is created by subclassing [unittest.TestCase].
    The individual tests are defined with methods whose names start with the letters [test_].
    This naming convention informs the test runner about which methods represent tests.

    The crux of each test is a call to :
        assertEqual() to check for an expected result;
        assertTrue() or assertFalse() to verify a condition;
        assertRaises() to verify that a specific exception gets raised.
    These methods are used instead of the assert statement
    so the test runner can accumulate all test results and produce a report.
    """
    def test_int(self):
        self.assertEqual(func(1, 2), 3)

    def test_float(self):
        self.assertEqual(func(1.0, 2.0), 3.0)

    def test_str(self):
        self.assertEqual(func('a', 'b'), 'ab')
    """
    The setUp() and tearDown() methods allow you to define instructions
    that will be executed before and after each test method.
    """
    def setUp(self):
        """
        Method called to prepare the test fixture. This is called immediately before calling the test method;
        other than AssertionError or SkipTest, any exception raised by this method will be considered an error
        rather than a test failure. The default implementation does nothing.
        """
        print 'unittest.setUp()'
        pass

    def tearDown(self):
        """
        Method called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception,
        so the implementation in subclasses may need to be particularly careful about checking internal state.
        Any exception, other than AssertionError or SkipTest,
        raised by this method will be considered an error rather than a test failure.
        This method will only be called if the setUp() succeeds, regardless of the outcome of the test method.
        The default implementation does nothing.
        """
        print 'unittest.tearDown()'
        pass


if __name__ == '__main__':
    """
    unittest.main() provides a command-line interface to the test script.
    """
    unittest.main()
