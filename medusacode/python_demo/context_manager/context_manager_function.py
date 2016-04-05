#!/usr/bin/env python
# coding:utf-8

"""
The contextlib module provides some functions and a decorator
that are useful when writing objects for use with the ‘with‘ statement.

The decorator is called contextmanager(), and lets you write a single generator function instead of defining a new class.
    The generator should yield exactly one value.
    The code up to the yield will be executed as the__enter__() method,
    and the value yielded will be the method’s return value that will get bound to
        the variable in the ‘with‘ statement’s as clause, if any.
    The code after the yield will be executed in the __exit__() method.
    Any exception raised in the block will be raised by the yield statement.
"""

from contextlib import contextmanager
import time
import requests


@contextmanager
def timer():
    start = time.time()
    try:
        yield None
    except:
        raise Exception
    else:
        stop = time.time()
        delta = stop - start
        print '(time consumed)', delta


with timer() as timer:
    response = requests.get(url='http://www.baidu.com', params={'wd': 'test'})
