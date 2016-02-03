#!/usr/bin/env python
# coding:utf-8


"""
面向切片编程(Aspect-Oriented Programming)
"""

import time


def timeit(f):
    def wrapper(*args, **kwargs):
        start = time.clock()
        ret = f(*args, **kwargs)
        stop = time.clock()
        print 'used:', stop-start
        print 'ret:', ret
        return ret
    return wrapper

@timeit
def func(a, b):
    print 'in func()'
    return a + b

r = func(1, 2)
print r
