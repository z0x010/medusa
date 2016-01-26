#!/usr/bin/env python
# coding:utf-8

"""
经典类和新式类
classic class and new-style class
"""

class ClassicClass:
    def __init__(self):
        pass
    pass

class NewstyleClass(object):
    def __init__(self):
        pass
    pass

cc = ClassicClass()
print cc.__class__    # __main__.ClassicClass
print type(cc)        # <type 'instance'>

nc = NewstyleClass()
print nc.__class__    # <class '__main__.NewstyleClass'>
print type(nc)        # <class '__main__.NewstyleClass'>


# 关于继承:
# 经典类的继承是深度优先;
# 新式类的继承是广度优先.
