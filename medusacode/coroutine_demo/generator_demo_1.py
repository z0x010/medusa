#!/usr/bin/env python
# coding=utf-8

"""
生成器(generator)
"""

"""
生成器表达式(generator expression)
"""
generator_1 = (n for n in xrange(5))
print type(generator_1)  # <type 'generator'>
print generator_1  # <generator object <genexpr> at 0x10ca93b40>

for item in generator_1:
    print item

"""
生成器函数(generator function)
"""
def generator_function():
    for n in xrange(5):
        yield n
print type(generator_function)  # <type 'function'>
print generator_function  # <function generator_function at 0x106176d70>

generator_2 = generator_function()
print type(generator_2)  # <type 'generator'>
print generator_2  # <generator object generator_function at 0x109e45dc0>

for i in range(5):
    print generator_2.next()
    pass
