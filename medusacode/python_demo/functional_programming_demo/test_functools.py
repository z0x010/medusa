#!/usr/bin/env python
# coding:utf-8

"""
functools — Higher-order functions and operations on callable objects
    The functools module is for higher-order functions: functions that act on or return other functions.
    In general, any callable object can be treated as a function for the purposes of this module.
"""

import functools


"""
functools.reduce(function, iterable[, initializer])
    This is the same function as reduce().
    It is made available in this module to allow writing code more forward-compatible with Python 3.
"""
print '--------------------------------------------------------------------------------------------------'
def func_reduce(x, y):
    return x+y

l = range(6)
ll = functools.reduce(func_reduce, l)
lll = functools.reduce(func_reduce, l, 100)
print l
# [0, 1, 2, 3, 4, 5]
print ll
# 15
print lll
# 115
print '--------------------------------------------------------------------------------------------------'


"""
functools.partial(func[,*args][, **keywords])
    Return a new partial object which when called will behave like
    func called with the positional arguments args and keyword arguments keywords.
    If more arguments are supplied to the call, they are appended to args.
    If additional keyword arguments are supplied, they extend and override keywords.
    Roughly equivalent to:

    def partial(func, *args, **keywords):
        def newfunc(*fargs, **fkeywords):
            newkeywords = keywords.copy()
            newkeywords.update(fkeywords)
            return func(*(args + fargs), **newkeywords)
        newfunc.func = func
        newfunc.args = args
        newfunc.keywords = keywords
        return newfunc

    The partial() is used for partial function application which “freezes” some portion of
    a function’s arguments and/or keywords resulting in a new object with a simplified signature.
    For example, partial() can be used to create a callable that behaves like the int() function
    where the base argument defaults to two:

    >>> from functools import partial
    >>> basetwo = partial(int, base=2)
    >>> basetwo.__doc__ = 'Convert base 2 string to an int.'
    >>> basetwo('10010')
    18
"""
print '--------------------------------------------------------------------------------------------------'
def func(*args, **kwargs):
    print args
    print kwargs
    return args, kwargs

ret = func(1, 2, 3, a=11, b=22, c=33)
# (1, 2, 3)
# {'a': 11, 'c': 33, 'b': 22}
print ret
# ((1, 2, 3), {'a': 11, 'c': 33, 'b': 22})

func_partial = functools.partial(func, 9, x=99)
ret_partial = func_partial(1, 2, 3, a=11, b=22, c=33)
# (9, 1, 2, 3)
# {'x': 99, 'a': 11, 'c': 33, 'b': 22}
print ret_partial
# ((9, 1, 2, 3), {'x': 99, 'a': 11, 'c': 33, 'b': 22})

print func_partial.func  # <function func at 0x1097bf938>
print func_partial.args  # (9,)
print func_partial.keywords  # {'x': 99}
print '--------------------------------------------------------------------------------------------------'


"""
functools.update_wrapper(wrapper, wrapped[, assigned][, updated])
    Update a wrapper function to look like the wrapped function.
    The optional arguments are tuples to specify
    which attributes of the original function are assigned directly to the matching attributes on the wrapper function
    and which attributes of the wrapper function are updated with the corresponding attributes from the original function.
    The default values for these arguments are the module level constants WRAPPER_ASSIGNMENTS
    (which assigns to the wrapper function’s __name__, __module__ and __doc__, the documentation string)
    and WRAPPER_UPDATES (which updates the wrapper function’s __dict__, i.e. the instance dictionary).

    The main intended use for this function is in decorator functions
    which wrap the decorated function and return the wrapper.
    If the wrapper function is not updated, the metadata of the returned function will
    reflect the wrapper definition rather than the original function definition,
    which is typically less than helpful.
"""

"""
functools.wraps(wrapped[, assigned][, updated])
    This is a convenience function for invoking update_wrapper() as a function decorator when defining a wrapper function.
    It is equivalent to partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated).
"""
print '--------------------------------------------------------------------------------------------------'
def my_decorator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print '(Calling decorated function)'
        return f(*args, **kwargs)
    return wrapper

@my_decorator
def func():
    """
    doc_string of func
    """
    print '(Calling original function)'


func()
# (Calling decorated function)
# (Calling original function)
print func.__name__
# func
print func.__module__
# __main__
print func.__doc__
# doc_string of func
print '--------------------------------------------------------------------------------------------------'
