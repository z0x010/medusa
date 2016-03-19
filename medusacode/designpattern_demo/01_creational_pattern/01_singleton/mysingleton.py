#!/usr/bin/env python
# coding:utf-8

"""
[单例模式]
[方法5][import]
作为python的模块是天然的单例模式
"""

"""
Python 真的需要单例模式吗?
答案是, 不需要!
因为, Python的模块(module), 就是最 pythonic 的单例典范。
模块在在一个应用程序中只有一份, 它本身就是单例的, 只要将所需要的属性和方法, 直接暴露在模块中变成模块的全局变量和全局方法即可!
"""

class My_Singleton(object):
    def foo(self):
        print id(self)

my_singleton = My_Singleton()

"""
# 在其他文件中使用:

from mysingleton import my_singleton
my_singleton.foo()
# 4473651024

from mysingleton import my_singleton
my_singleton.foo()
# 4473651024
"""
