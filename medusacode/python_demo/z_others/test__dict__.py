#!/usr/bin/env python
# coding:utf-8


"""
In Python, everything is an object containing attributes.
That includes classes themselves.
The whole object-oriented thing with classes which define methods and instances
which can execute those methods with the varying data per-instance is
just a protocol for looking up attributes in a series of objects.
"""

class MyClass(object):
    attr = 1

    def __init__(self):
        self.a = None
        self.b = None

    def geta(self):
        return self.a

    def getb(self):
        return self.a

    pass

mc = MyClass()
print MyClass.__dict__
# {
#   '__module__': '__main__',
#   'attr': 1,
#   'geta': <functiongetaat0x107bc5f50>,
#   'getb': <functiongetbat0x107bd8050>,
#   '__dict__': <attribute'__dict__'of'MyClass'objects>,
#   '__weakref__': <attribute'__weakref__'of'MyClass'objects>,
#   '__doc__': None,
#   '__init__': <function__init__at0x107bc5ed8>
# }
print mc.__dict__
# {
#   'a': None,
#   'b': None
# }
print dir(MyClass)
print dir(mc)
