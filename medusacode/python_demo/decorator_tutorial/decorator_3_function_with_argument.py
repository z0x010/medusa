#!/usr/bin/env python
# coding:utf-8


# It’s not black magic, you just have to let the [wrapper] pass the argument:

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print "I got args! Look:", arg1, arg2
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

# Since when you are calling the function returned by the decorator,
# you are calling the [wrapper],
# passing arguments to the [wrapper] will let it pass them to the [decorated function]

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print "My name is", first_name, last_name

print_full_name("Peter", "Venkman")
# outputs:
# I got args! Look: Peter Venkman
# My name is Peter Venkman
