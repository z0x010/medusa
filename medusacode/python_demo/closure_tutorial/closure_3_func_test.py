#!/usr/bin/env python
# coding:utf-8

def foo():
    x = 3

    def bar():
      print x
    x = 5
    return bar


b = foo()
b()   # print 5


"""
A key idea is:
the function object (bar) returned from foo retains a hook to the local var 'x',
even though 'x' has gone out of scope and should be defunct.

This hook is to the var itself, not just the value that var had at the time,
so when bar is called, it prints 5, not 3.

Also be clear that Python 2.x has limited closure:
there's no way I can modify 'x' inside 'bar' because writing 'x = bla' would declare a local 'x' in bar, not assign to 'x' of foo.
This is a side-effect of Python's assignment=declaration.
To get around this, Python 3.0 introduces the keyword: nonlocal
"""
