#!/usr/bin/env python
# coding:utf-8

import pdb
import ipdb
import sys

print id(123454321)

a = 123454321
b = a

print id(123454321)
print id(a)
print id(b)

print sys.getrefcount(a)
del b
print sys.getrefcount(a)
