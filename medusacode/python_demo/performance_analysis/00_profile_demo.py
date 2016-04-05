#!/usr/bin/env python
# coding:utf-8

"""
Both the profile and cProfile modules provide the following functions:

profile.run(command, filename=None, sort=-1)
    This function takes a single argument that can be passed to the exec() function, and an optional file name.
    In all cases this routine executes:
    exec(command, __main__.__dict__, __main__.__dict__)
    and gathers profiling statistics from the execution.
    If no file name is present, then this function automatically creates a Stats instance
    and prints a simple profiling report.
    If the sort value is specified it is passed to this Stats instance to control how the results are sorted.

profile.runctx(command, globals, locals, filename=None)
    This function is similar to run(),
    with added arguments to supply the globals and locals dictionaries for the command string.
    This routine executes:
    exec(command, globals, locals)
    and gathers profiling statistics as in the run() function above.
"""

import profile

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

# print calculate(10000)

# [1]
# profile.run(statement='calculate(10000)')
# [2]
profile.runctx(statement='calculate(10000)', globals=globals(), locals=locals())

"""
         6 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.002    0.002 00_profile_demo.py:26(calculate)
        2    0.000    0.000    0.000    0.000 :0(range)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.000    0.000    0.003    0.003 profile:0(calculate(10000))
        0    0.000             0.000          profile:0(profiler)

"""
