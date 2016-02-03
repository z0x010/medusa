#!/usr/bin/env python
# coding:utf-8

"""
Decorators wrap functions, which can make them hard to debug. (This gets better from Python >= 2.5; see below.)
The functools module was introduced in Python 2.5.
It includes the function functools.wraps(), which copies the name, module, and docstring of the decorated function to its wrapper.
# Fun fact: functools.wraps() is a decorator! ☺
"""

print '--------------------------------------------------------------------------------------------------------------'
# For debugging, the stacktrace prints you the function __name__
def foo():
    print "foo"

print foo.__name__
# outputs: foo


# With a decorator, it gets messy
def bar(func):
    def wrapper():
        print "bar"
        return func()
    return wrapper

@bar
def foo():
    print "foo"

print foo.__name__
# outputs: wrapper

print '--------------------------------------------------------------------------------------------------------------'
# "functools" can help for that

import functools

def bar(func):
    # We say that "wrapper", is wrapping "func"
    # and the magic begins
    @functools.wraps(func)
    def wrapper():
        print "bar"
        return func()
    return wrapper

@bar
def foo():
    print "foo"

print foo.__name__
# outputs: foo
print '--------------------------------------------------------------------------------------------------------------'
