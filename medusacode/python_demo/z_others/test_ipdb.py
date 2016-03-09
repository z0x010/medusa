#!/usr/bin/env python
# coding:utf-8

import pdb
import ipdb

def func_add(x, y):
    print x, y
    add = x + y
    ipdb.set_trace()
    return add

a = 1
b = 2
ipdb.set_trace()
c = func_add(a, b)
ipdb.set_trace()
d = a + b + c
