#!/usr/bin/env python
# coding:utf-8

print '--------------------------------------------------------------------------------------------------'
# 装饰器
def decorator(f):
    def new_func(a, b):
        print "original func: func"
        print str(f)
        print "decoratored func: new_func"
        print str(new_func)
        return f(a, b)
    return new_func

# 函数 1
@decorator
def func_1(a, b):
    return a + b

print func_1(1, 2)
print '--------------------------------------------------------------------------------------------------'
# 带参数的装饰器
def decorator_extra(extra=''):
    def decorator_2(f):
        def new_func(a, b):
            print "extra", extra
            print "original func: func"
            print str(f)
            print "decoratored func: new_func"
            print str(new_func)
            return f(a, b)
        return new_func
    return decorator_2

# 函数 2
@decorator_extra(extra='test_extra')
def func_2(a, b):
    return a - b

print func_2(1, 2)
print '--------------------------------------------------------------------------------------------------'
