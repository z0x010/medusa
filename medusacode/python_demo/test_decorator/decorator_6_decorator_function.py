#!/usr/bin/env python
# coding:utf-8


# Decorators are ORDINARY functions
def my_decorator(func):
    print "I am an ordinary function"
    def wrapper():
        print "I am function returned by the decorator"
        func()
    return wrapper
# Therefore, you can call it without any "@"

def lazy_function():
    print "zzzzzzzz"

decorated_function = my_decorator(lazy_function)
# outputs: I am an ordinary function
# It outputs "I am an ordinary function", because that’s just what you do:
# calling a function. Nothing magic.

@my_decorator
def lazy_function():
    print "zzzzzzzz"

# outputs: I am an ordinary function
# It’s exactly the same. "my_decorator" is called.
# So when you @my_decorator, you are telling Python to call the function 'labelled by the variable "my_decorator"'.
# This is important! The label you give can point directly to the decorator—or not.


