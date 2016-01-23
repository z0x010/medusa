#!/usr/bin/env python
# coding:utf-8


def benchmark(func):
    """
    A decorator that prints the time a function takes to execute.
    """
    import time

    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print func.__name__, time.clock()-t
        return res
    return wrapper


def logging(func):
    """
    A decorator that logs the activity of the script.
    (it actually just prints it, but it could be logging!)
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print func.__name__, args, kwargs
        return res
    return wrapper


def counter(func):
    """
    A decorator that counts and prints the number of times a function has been executed
    """
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print "{0} has been used: {1} times".format(func.__name__, wrapper.count)
        return res
    wrapper.count = 0
    return wrapper


@counter
@benchmark
@logging
def reverse_string(string):
    return str(reversed(string))

print reverse_string("Able was I ere I saw Elba")
# outputs:
# reverse_string ('Able was I ere I saw Elba',) {}
# wrapper 4.7e-05
# wrapper has been used: 1 times
# <reversed object at 0x105392e50>

print reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe.")
# outputs:
# reverse_string ('A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe.',) {}
# wrapper 5.1e-05
# wrapper has been used: 2 times
# <reversed object at 0x105392e50>

