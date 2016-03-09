#!/usr/bin/env python
# coding:utf-8

"""
经典类和新式类
classic class and new-style class
"""

import inspect

print '----------------------------------------------------------------------------------------------------'
class ClassicClass:
    def __init__(self):
        pass
    pass

class NewstyleClass(object):
    def __init__(self):
        pass
    pass
print '----------------------------------------------------------------------------------------------------'
print dir(ClassicClass)
# [
#   '__doc__',
#   '__init__',
#   '__module__'
# ]
print ClassicClass.__dict__
# {
#   '__module__': '__main__',
#   '__doc__': None,
#   '__init__': <function__init__at0x10a9510c8>
# }
print '----------------------------------------------------------------------------------------------------'
print dir(NewstyleClass)
# [
#   '__class__',
#   '__delattr__',
#   '__dict__',
#   '__doc__',
#   '__format__',
#   '__getattribute__',
#   '__hash__',
#   '__init__',
#   '__module__',
#   '__new__',
#   '__reduce__',
#   '__reduce_ex__',
#   '__repr__',
#   '__setattr__',
#   '__sizeof__',
#   '__str__',
#   '__subclasshook__',
#   '__weakref__'
# ]
print NewstyleClass.__dict__
# {
#   '__dict__': <attribute'__dict__'of'NewstyleClass'objects>,
#   '__module__': '__main__',
#   '__weakref__': <attribute'__weakref__'of'NewstyleClass'objects>,
#   '__doc__': None,
#   '__init__': <function__init__at0x10a9512a8>
# }
print '----------------------------------------------------------------------------------------------------'
cc = ClassicClass()
print cc.__class__    # __main__.ClassicClass
print type(cc)        # <type 'instance'>

nc = NewstyleClass()
print nc.__class__    # <class '__main__.NewstyleClass'>
print type(nc)        # <class '__main__.NewstyleClass'>
print '----------------------------------------------------------------------------------------------------'

# 关于继承:
# 经典类的继承是深度优先;
# 新式类的继承是广度优先.
