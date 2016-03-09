#!/usr/bin/env python
# coding:utf-8

"""
Functional Programming
"""


# [map]
print '--------------------------------------------------------------------------------------------------'
def func_map(x):
    return x**2

l = range(10)
ll = map(func_map, l)
print l
print ll
print '--------------------------------------------------------------------------------------------------'


# [reduce]
print '--------------------------------------------------------------------------------------------------'
def func_reduce(x, y):
    return x+y

l = range(6)
ll = reduce(func_reduce, l)
lll = reduce(func_reduce, l, 100)
print l
print ll
print lll
print '--------------------------------------------------------------------------------------------------'


# [filter]
print '--------------------------------------------------------------------------------------------------'
def is_prime(x):
    if x <= 2:
        return False
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True

l = range(100)
ll = filter(is_prime, l)
print ll
print '--------------------------------------------------------------------------------------------------'
