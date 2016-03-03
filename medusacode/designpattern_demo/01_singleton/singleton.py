#!/usr/bin/env python
# coding:utf-8


"""
单例模式实现方法
"""
print '===================================================================================================='
"""
[方法1][共享实例]
实现__new__方法，并将一个类的实例绑定到类变量_instance上，
如果cls._instance为None说明该类还没有实例化过，实例化该类，并返回；
如果cls._instance非None说明该类已经被实例化过，直接返回cls._instance；
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
[方法2][共享属性]
创建实例时，将所有实例的__dict__指向同一个字典(dict)，使得它们具有相同的属性和方法。
"""
"""
所谓单例就是所有引用(实例、对象)拥有相同的状态(属性)和行为(方法)。
同一个类的所有实例天然拥有相同的行为(方法)，只需要保证同一个类的所有实例具有相同的状态(属性)即可。
对任何实例的名字属性的设置，无论是在__init__中修改还是直接修改，所有的实例都会受到影响。不过实例的id是不同的。
"""
"""
object.__dict__
    A dictionary or other mapping object used to store an object’s (writable) attributes.
注意区分:
    class.__dict__
    instance.__dict__
"""

class Bravo(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Bravo, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state  # instance.__dict__ = class._shared_state
        return obj

class MyClass2(Bravo):
    x = 1
    pass

a = MyClass2()
b = MyClass2()

a.x = 9

print a, id(a)
print b, id(b)
# <__main__.MyClass2 object at 0x10defec50> 4528794704
# <__main__.MyClass2 object at 0x10defecd0> 4528794832
print a.x, id(a.x), a.__dict__, id(a.__dict__), id(Bravo._shared_state)
print b.x, id(b.x), b.__dict__, id(b.__dict__), id(Bravo._shared_state)
# 9 140325309983816 {'x': 9} 140325311114016 140325311114016
# 9 140325309983816 {'x': 9} 140325311114016 140325311114016
print Bravo._shared_state, id(Bravo._shared_state)
# {'x': 9} 140325311114016
print '===================================================================================================='
"""
[方法3][装饰器]
其实是方法1的升级（高级）版，
使用装饰器(decorator)，这是更加pythonic、更加elegant的方法。
"""

def singleton(cls, *args, **kwargs):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton

@singleton
class MyClass3(object):
    ca = 1
    def __init__(self, x=0):
        self.x = x

a = MyClass3()
b = MyClass3()

print a, id(a)
print b, id(b)
a.ca = 9
print a.ca, id(a.ca)
print b.ca, id(b.ca)

# 使用 @singleton 修饰前
# <__main__.MyClass3 object at 0x10d458e10> 4517629456
# <__main__.MyClass3 object at 0x10d458d90> 4517629328
# 9 140491095055720
# 1 140491095055912

# 使用 @singleton 修饰后
# <__main__.MyClass3 object at 0x106dffe10> 4410310160
# <__main__.MyClass3 object at 0x106dffe10> 4410310160
# 9 140683822311880
# 9 140683822311880
print '===================================================================================================='
"""
[方法4][import]
作为python的模块是天然的单例模式
"""
"""
# 在其他模块文件（mysingleton.py）中定义:

class My_Singleton(object):
    def foo(self):
        pass

my_singleton = My_Singleton()
"""

# 在当前模块文件中使用
from mysingleton import my_singleton
my_singleton.foo()
# 4473651024
from mysingleton import my_singleton
my_singleton.foo()
# 4473651024
print '===================================================================================================='
