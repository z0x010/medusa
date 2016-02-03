#!/usr/bin/env python
# coding:utf-8


def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        # very friendly, decrease age even more :-)
        lie = lie - 3
        method_to_decorate(self, lie)
    return wrapper


class Lucy(object):

    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print "I am %s, what did you think?" % (self.age + lie)


l = Lucy()
l.sayYourAge(-3)
# outputs: I am 26, what did you think?
