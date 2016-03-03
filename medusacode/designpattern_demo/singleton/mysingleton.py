#!/usr/bin/env python
# coding:utf-8

"""
[单例模式]
[方法4][import]
作为python的模块是天然的单例模式
"""

class My_Singleton(object):
    def foo(self):
        print id(self)
        pass

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
