#!/usr/bin/env python
# coding:utf-8

"""
Python 类属性和实例属性:
    1. Python中属性的获取是按照从下到上的顺序来查找属性；
    2. Python中的类和实例是两个完全独立的对象；
    3. Python中的属性设置是针对对象本身进行的；

Python 作为一个动态语言，在OOP的机制上与静态语言的差别。
最关键的地方在于两点:
    1. 理解Python是如何利用查找树的机制来模仿类及实例之间的关系；
    2. 理解动态语言是可以动态设置属性的；
"""

class base:
    x = 1
    pass

a = base()
b = base()

print base.__dict__  # {'x': 1, '__module__': '__main__', '__doc__': None}
print a.__dict__  # {}
print b.__dict__  # {}
print id(base.x), base.x  # 140276102410120 1
print id(a.x), a.x  # 140276102410120 1
print id(b.x), b.x  # 140276102410120 1

a.x += 1
print base.__dict__  # {'x': 1, '__module__': '__main__', '__doc__': None}
print a.__dict__  # {'x': 2}
print b.__dict__  # {}
print id(base.x), base.x  # 140276102410120 1
print id(a.x), a.x  # 140276102410096 2
print id(b.x), b.x  # 140276102410120 1

base.x += 2
print base.__dict__  # {'x': 3, '__module__': '__main__', '__doc__': None}
print a.__dict__  # {'x': 2}
print b.__dict__  # {}
print id(base.x), base.x  # 140276102410072 3
print id(a.x), a.x  # 140276102410096 2
print id(b.x), b.x  # 140276102410072 3
