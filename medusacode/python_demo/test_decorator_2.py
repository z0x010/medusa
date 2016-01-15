#!/usr/bin/env python
# coding:utf-8

import time
import datetime

# 定义一个计时器，传入一个函数，并返回另一个附加了计时功能的函数
def timeit(f):
    # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
    def wrapper():
        print 'wrapper start'
        start = datetime.datetime.now()
        f()
        end = datetime.datetime.now()
        print '[used]', end - start
        print 'wrapper stop'
    # 将包装后的函数返回
    return wrapper

@timeit
def func():
    print 'func start'
    time.sleep(1)
    print 'func stop'

func()
