#!/usr/bin/env python
# coding:utf-8

"""
"""

@profile
def calculate(n):
    s = 0
    for i in range(n):
        s += i
    for i in xrange(n):
        s += i
    for i in range(n):
        s *= i
    for i in xrange(n):
        s *= i
    return s

print calculate(10000)

"""
vagrant@precise64:~$ python -m memory_profiler memory_profiler_demo.py
0
Filename: memory_profiler_demo.py

Line #    Mem usage    Increment   Line Contents
================================================
     7   18.402 MiB    0.000 MiB   @profile
     8                             def calculate(n):
     9   18.402 MiB    0.000 MiB       s = 0
    10   18.727 MiB    0.324 MiB       for i in range(n):
    11   18.727 MiB    0.000 MiB           s += i
    12   18.727 MiB    0.000 MiB       for i in xrange(n):
    13   18.727 MiB    0.000 MiB           s += i
    14   18.898 MiB    0.172 MiB       for i in range(n):
    15   18.898 MiB    0.000 MiB           s *= i
    16   18.898 MiB    0.000 MiB       for i in xrange(n):
    17   18.898 MiB    0.000 MiB           s *= i
    18   18.898 MiB    0.000 MiB       return s
"""
