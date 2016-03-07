#!/usr/bin/env python
# coding=utf-8

"""
生成器(generator)
生成器函数(generator function)
"""

"""

generator.next()
    Starts the execution of a generator function or resumes it at the last executed yield expression.
    When a generator function is resumed with a next() method, the current yield expression always evaluates to None.
    The execution then continues to the next yield expression, where the generator is suspended again,
    and the value of the expression_list is returned to next()‘s caller.
    If the generator exits without yielding another value, a StopIteration exception is raised.

generator.send(value)
    Resumes the execution and “sends” a value into the generator function.
    The value argument becomes the result of the current yield expression.
    The send() method returns the next value yielded by the generator,
    or raises StopIteration if the generator exits without yielding another value.
    When send() is called to start the generator, it must be called with None as the argument,
    because there is no yield expression that could receive the value.

generator.throw(type[, value[, traceback]])
    Raises an exception of type type at the point where generator was paused,
    and returns the next value yielded by the generator function.
    If the generator exits without yielding another value, a StopIteration exception is raised.
    If the generator function does not catch the passed-in exception, or raises a different exception,
    then that exception propagates to the caller.

generator.close()
    Raises a GeneratorExit at the point where the generator function was paused.
    If the generator function then raises StopIteration (by exiting normally, or due to already being closed)
    or GeneratorExit (by not catching the exception), close returns to its caller.
    If the generator yields a value, a RuntimeError is raised.
    If the generator raises any other exception, it is propagated to the caller.
    close() does nothing if the generator has already exited due to an exception or normal exit.
"""

def generator_function(value=None):
    print 'next() is called for the first time'
    try:
        while True:
            try:
                # yield value
                value = yield value
                print '...... value=', value
            except Exception, e:
                print type(e), e
                value = e
    finally:
        print 'do not forget to call close()'


generator = generator_function(1)
print generator.next()
# 1
print generator.next()
# None
print generator.send(22)
# 22
print generator.next()
# None
print generator.throw(TypeError, 'spam')
# spam
print generator.close()
# None
