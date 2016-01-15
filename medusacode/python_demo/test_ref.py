#!/usr/bin/env python
# coding:utf-8

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
