#!/usr/bin/env python
# coding:utf-8


def benchmark(func):
    """
    A decorator that prints the time a function takes to execute.
    """
    import time

    def wrapper(*args, **kwargs):
        start = time.clock()
        res = func(*args, **kwargs)
        stop = time.clock()
        print '[benchmark]', func.__name__, stop - start
        return res
    return wrapper


def logging(func):
    """
    A decorator that logs the activity of the script.
    (it actually just prints it, but it could be logging!)
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print '[logging]', func.__name__, args, kwargs
        return res
    return wrapper


def counter(func):
    """
    A decorator that counts and prints the number of times a function has been executed
    """
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print '[counter]', "{0} has been used: {1} times".format(func.__name__, wrapper.count)
        return res
    wrapper.count = 0
    return wrapper


@counter
@benchmark
@logging
def reverse_string(string):
    return str(reversed(string))

print reverse_string("123456789")
# outputs:
# [logging] reverse_string ('123456789',) {}
# [benchmark] wrapper 4e-05
# [counter] wrapper has been used: 1 times
# <reversed object at 0x109517d90>

print reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe.")
# outputs:
# [logging] reverse_string ('A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe.',) {}
# [benchmark] wrapper 4.9e-05
# [counter] wrapper has been used: 2 times
# <reversed object at 0x109517d90>
