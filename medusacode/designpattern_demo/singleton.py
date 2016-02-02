#!/usr/bin/env python
# coding:utf-8


print '===================================================================================================='
"""
方法1
实现__new__方法,并将一个类的实例绑定到类变量_instance上,
如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回;
如果cls._instance非None说明该类已经被实例化过,直接返回cls._instance;
"""
"""
在 Java 中，
静态变量(在Python中叫类属性)和实例变量(在Python中叫数据属性)两者都是紧跟在类定义之后定义的(一个有static关键字，一个没有)。
在 Python 中，
只有类属性可以紧跟在类定义之后定义，数据属性定义在__init__方法中。
"""
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance  # class attribute !!!!!

class MyClass(Singleton):
    pass

a = MyClass()
b = MyClass()
print a, id(a)
print b, id(b)
# <__main__.MyClass object at 0x102113a50> 4329650768
# <__main__.MyClass object at 0x102113a50> 4329650768
print '===================================================================================================='
print '===================================================================================================='
print '===================================================================================================='
print '===================================================================================================='
