#!/usr/bin/env python
# coding:utf-8


def decorator_maker():

    print "I am a decorator_maker! I am executed only once: when you make me create a decorator."

    def my_decorator(func):

        print "I am a decorator! I am executed only when you decorate a function."

        def wrapped():
            print ("I am the wrapper around the decorated function! I am called when you call the decorated function. "
                   "As a wrapper, I RETURN the RESULT of the decorated function.")
            return func()

        print "As a decorator, I return the wrapped function."
        return wrapped

    print "As a decorator_maker, I return a decorator"
    return my_decorator

print '--------------------------------------------------------------------------------------------------------------'
# Let’s create a decorator. It’s just a new function after all.
new_decorator = decorator_maker()
# outputs:
# I am a decorator_maker! I am executed only once: when you make me create a decorator.
# As a decorator_maker, I return a decorator

# Then we decorate the function
def decorated_function():
    print "I am the decorated function."

decorated_function = new_decorator(decorated_function)
# outputs:
# I am a decorator! I am executed only when you decorate a function.
# As a decorator, I return the wrapped function

# Let’s call the function:
decorated_function()
# outputs:
# I am the wrapper around the decorated function. I am called when you call the decorated function.
# As a wrapper, I return the RESULT of the decorated function.
# I am the decorated function.
print '--------------------------------------------------------------------------------------------------------------'
# Let’s do EXACTLY the same thing, but skip all the pesky intermediate variables:

def decorated_function():
    print "I am the decorated function."
decorated_function = decorator_maker()(decorated_function)
# outputs:
# I am a decorator_maker! I am executed only once: when you make me create a decorator.
# As a decorator_maker, I return a decorator
# I am a decorator! I am executed only when you decorate a function.
# As a decorator, I return the wrapped function.

# Finally:
decorated_function()
# outputs:
# I am the wrapper around the decorated function. I am called when you call the decorated function.
# As a wrapper, I return the RESULT of the decorated function.
# I am the decorated function.
print '--------------------------------------------------------------------------------------------------------------'
# Let’s make it even shorter:

@decorator_maker()
def decorated_function():
    print "I am the decorated function."
# outputs:
# I am a decorator_maker! I am executed only once: when you make me create a decorator.
# As a decorator_maker, I return a decorator
# I am a decorator! I am executed only when you decorate a function.
# As a decorator, I return the wrapped function.

# Eventually:
decorated_function()
# outputs:
# I am the wrapper around the decorated function. I am called when you call the decorated function.
# As a wrapper, I return the RESULT of the decorated function.
# I am the decorated function.

# Hey, did you see that? We used a function call with the "@" syntax!
print '--------------------------------------------------------------------------------------------------------------'
# So, back to decorators with arguments.
# If we can use functions to generate the decorator on the fly, we can pass arguments to that function, right?

def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):

    print "I am a decorator_maker! I am executed only once: when you make me create a decorator. And I accept arguments:", decorator_arg1, decorator_arg2

    def my_decorator(func):
        # The ability to pass arguments here is a gift from closures.
        # If you are not comfortable with closures, you can assume it’s ok,
        # or read: http://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python
        print "I am a decorator! I am executed only when you decorate a function. Somehow you passed me arguments:", decorator_arg1, decorator_arg2

        # Don't confuse decorator arguments and function arguments!
        def wrapped(function_arg1, function_arg2):
            print ("I am the wrapper around the decorated function! I am called when you call the decorated function. I can access all the variables\n"
                   "\t- from the decorator: {0} {1}\n"
                   "\t- from the function call: {2} {3}\n"
                   "Then I can pass them to the decorated function"
                   .format(decorator_arg1, decorator_arg2,
                           function_arg1, function_arg2))
            return func(function_arg1, function_arg2)

        print "As a decorator, I return the wrapped function."
        return wrapped

    print "As a decorator_maker, I return a decorator"
    return my_decorator

@decorator_maker_with_arguments("Leonard", "Sheldon")
def decorated_function_with_arguments(function_arg1, function_arg2):
    print ("I am the decorated function and only knows about my arguments: {0} {1}".format(function_arg1, function_arg2))
# outputs:
# I am a decorator_maker! I am executed only once: when you make me create a decorator. And I accept arguments: Leonard Sheldon
# As a decorator_maker, I return a decorator
# I am a decorator! I am executed only when you decorate a function. Somehow you passed me arguments: Leonard Sheldon
# As a decorator, I return the wrapped function.

decorated_function_with_arguments("Rajesh", "Howard")
# outputs:
# I am the wrapper around the decorated function! I am called when you call the decorated function. I can access all the variables
# 	- from the decorator: Leonard Sheldon
# 	- from the function call: Rajesh Howard
# Then I can pass them to the decorated function
# I am the decorated function and only knows about my arguments: Rajesh Howard
print '--------------------------------------------------------------------------------------------------------------'
# Here it is: a decorator with arguments.
# Arguments can be set as variable:

c1 = "Penny"
c2 = "Leslie"

@decorator_maker_with_arguments("Leonard", c1)
def decorated_function_with_arguments(function_arg1, function_arg2):
    print ("I am the decorated function and only knows about my arguments: {0} {1}".format(function_arg1, function_arg2))
# outputs:
# I am a decorator_maker! I am executed only once: when you make me create a decorator. And I accept arguments: Leonard Penny
# As a decorator_maker, I return a decorator
# I am a decorator! I am executed only when you decorate a function. Somehow you passed me arguments: Leonard Penny
# As a decorator, I return the wrapped function.

decorated_function_with_arguments(c2, "Howard")
# outputs:
# I am the wrapper around the decorated function. I can access all the variables
# 	- from the decorator: Leonard Penny
# 	- from the function call: Leslie Howard
# Then I can pass them to the decorated function
# I am the decorated function and only knows about my arguments: Leslie Howard


# As you can see, you can pass arguments to the decorator like any function using this trick.
# You can even use *args, **kwargs if you wish.
# But remember decorators are called ONLY ONCE. Just when Python imports the script(when you decorate a function).
# You can't dynamically set the arguments afterwards.
# When you do "import x", the function is already decorated, so you can't change anything.
print '--------------------------------------------------------------------------------------------------------------'
