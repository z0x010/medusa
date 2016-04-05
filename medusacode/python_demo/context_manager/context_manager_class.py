#!/usr/bin/env python
# coding:utf-8

"""
the context management protocol
(that is, has __enter__() and __exit__() methods)

__enter__()
    The object’s __enter__() is called before with-block is executed and therefore can run set-up code.
    It also may return a value that is bound to the name variable, if given.
    (Note carefully that variable is not assigned the result of expression.)
__exit__()
    After execution of the with-block is finished, the object’s __exit__() method is called,
    even if the block raised an exception, and can therefore run clean-up code.
"""

import time
import requests


class Timer(object):
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.time()
        self.delta = self.stop - self.start
        print '(time consumed)', self.delta


with Timer() as timer:
    response = requests.get(url='http://www.baidu.com', params={'wd': 'test'})
