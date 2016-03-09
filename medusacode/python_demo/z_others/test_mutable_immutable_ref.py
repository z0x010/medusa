#!/usr/bin/env python
# coding:utf-8

"""
可变对象(mutable): list, dict, set
不可变对象(immutable): tuple, frozenset

Python 函数参数:
对于可变对象，函数内对参数的改变会影响到原始对象；
对于不可变对象，函数内对参数的改变不会影响到原始参数。
原因在于:
1、可变对象，参数改变的是可变对象，其内容可以被修改。
2、不可变对象，改变的是函数内变量的指向对象。
"""

# 值传递和地址传递

# 值传递
def func_1(arg):
    arg = arg + 1
    return arg

v = 1
print v
print func_1(v)
print v

# 地址传递
def func_2(iterable):
    for n in range(len(iterable)):
        iterable[n] = iterable[n] + 10
        pass
    return iterable

l = [1, 2, 3]
print l
print func_2(l)
print l
