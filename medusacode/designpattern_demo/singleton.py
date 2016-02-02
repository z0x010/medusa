#!/usr/bin/env python
# coding:utf-8


"""
单例模式实现方法
"""
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
"""
方法2
共享属性,所谓单例就是所有引用(实例、对象)拥有相同的状态(属性)和行为(方法)
同一个类的所有实例天然拥有相同的行为(方法),
只需要保证同一个类的所有实例具有相同的状态(属性)即可。
所有实例共享属性的最简单最直接的方法就是__dict__属性指向(引用)同一个字典(dict)。
"""
"""
object.__dict__
    A dictionary or other mapping object used to store an object’s (writable) attributes.
注意区分:
    class.__dict__
    instance.__dict__
"""

class Borg(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state  # instance.__dict__ = class._shared_state
        return obj

class MyClass2(Borg):
    x = 1
    pass

a = MyClass2()
b = MyClass2()

a.x = 9

print a, id(a)
print b, id(b)
# <__main__.MyClass2 object at 0x10defec50> 4528794704
# <__main__.MyClass2 object at 0x10defecd0> 4528794832
print a.x, id(a.x), a.__dict__, id(a.__dict__), id(Borg._shared_state)
print b.x, id(b.x), b.__dict__, id(b.__dict__), id(Borg._shared_state)
# 9 140325309983816 {'x': 9} 140325311114016 140325311114016
# 9 140325309983816 {'x': 9} 140325311114016 140325311114016
print Borg._shared_state, id(Borg._shared_state)
# {'x': 9} 140325311114016
print '===================================================================================================='
print '===================================================================================================='
print '===================================================================================================='
