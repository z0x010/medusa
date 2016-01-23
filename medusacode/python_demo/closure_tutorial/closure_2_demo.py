#!/usr/bin/env python
# coding:utf-8

"""
A closure is a function that references variables from a containing scope,
potentially after flow-of-control has left that scope. (That last bit is very useful)
"""
"""
A closure allows you to bind variables into a function without passing them as parameters.
"""

def makeConstantAdder(x):
    constant = x

    def adder(y):  # adder() is a closure (also a object)
        return y + constant
    return adder

f = makeConstantAdder(12)
print f(3)
# 15

g = makeConstantAdder(4)
print g(3)
# 7
