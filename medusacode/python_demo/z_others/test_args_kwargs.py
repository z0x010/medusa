#!/usr/bin/env python
# coding:utf-8

def func(a, b, c):
    return a+b+c


# 星号起到的作用是参数拆分:
# 将l中的每一个元素都作为独立的参数赋给func函数。
l = (1, 2, 3)
print func(*l)
# 上述代码等价于如下代码:
print func(1, 2, 3)


# 星号起到的作用是参数拆分:
# 将d中的每一个键值对都作为独立的参数赋给func函数。
d = {
    'a': 1,
    'b': 2,
    'c': 3,
}
print func(**d)
# 上述代码等价于如下代码:
print func(a=1, b=2, c=3)
