#!/usr/bin/env python
# coding:utf-8

"""
Process Pools
"""
"""
The Pool class represents a pool of worker processes.
It has methods which allows tasks to be offloaded to the worker processes in a few different ways.
One can create a pool of processes which will carry out tasks submitted to it with the Pool class.
"""
"""
class multiprocessing.Pool([processes[, initializer[, initargs[, maxtasksperchild]]]])
    A process pool object which controls a pool of worker processes to which jobs can be submitted.
    It supports asynchronous results with timeouts and callbacks and has a parallel map implementation.
    Note that the methods of the pool object should only be called by the process which created the pool.

    processes is the number of worker processes to use.
    If processes is None then the number returned by cpu_count() is used.
    If initializer is not None then each worker process will call initializer(*initargs) when it starts.
    maxtasksperchild is the number of tasks a worker process can complete
        before it will exit and be replaced with a fresh worker process,
        to enable unused resources to be freed.
        The default maxtasksperchild is None, which means worker processes will live as long as the pool.

    (built-in function)
    apply(function, args[, keywords])
        The function argument must be a callable object and the args argument must be a sequence.
        The function is called with args as the argument list;
        the number of arguments is the length of the tuple.
        If the optional keywords argument is present, it must be a dictionary whose keys are strings.
        It specifies keyword arguments to be added to the end of the argument list.

        Calling apply() is different from just calling function(args),
        since in that case there is always exactly one argument.
        The use of apply() is equivalent to function(*args, **keywords).

    apply(func[, args[, kwds]])
        Equivalent of the apply() built-in function.
        It blocks until the result is ready, so apply_async() is better suited for performing work in parallel.
        Additionally, func is only executed in one of the workers of the pool.
    apply_async(func[, args[, kwds[, callback]]])
        A variant of the apply() method which returns a result object.
        If callback is specified then it should be a callable which accepts a single argument.
        When the result becomes ready callback is applied to it (unless the call failed).
        callback should complete immediately since otherwise the thread which handles the results will get blocked.

    map(func, iterable[, chunksize])
        A parallel equivalent of the map() built-in function (it supports only one iterable argument though).
        It blocks until the result is ready.
        This method chops the iterable into a number of chunks which it submits to the process pool as separate tasks.
        The (approximate) size of these chunks can be specified by setting chunksize to a positive integer.

    map_async(func, iterable[, chunksize[, callback]])
        A variant of the map() method which returns a result object.
        If callback is specified then it should be a callable which accepts a single argument.
        When the result becomes ready callback is applied to it (unless the call failed).
        callback should complete immediately since otherwise the thread which handles the results will get blocked.
"""
"""
class multiprocessing.pool.AsyncResult
    The class of the result returned by Pool.apply_async() and Pool.map_async().

    get([timeout])
        Return the result when it arrives.
        If timeout is not None and the result does not arrive within timeout seconds
        then multiprocessing.TimeoutError is raised.
        If the remote call raised an exception then that exception will be reraised by get().

    wait([timeout])
        Wait until the result is available or until timeout seconds pass.

    ready()
        Return whether the call has completed.

    successful()
        Return whether the call completed without raising an exception.
        Will raise AssertionError if the result is not ready.
"""

from multiprocessing import Process, Queue, Pipe, Lock, RLock, Value, Array, Manager, Pool
import os
import time
import datetime
import random
import Queue as QUEUE

def worker(arg):
    print '..........(worker start)', '[worker](pid:%s ppid:%s)' % (os.getpid(), os.getppid())
    time.sleep(random.random())
    print '..........(worker stop)', '[worker](pid:%s ppid:%s)' % (os.getpid(), os.getppid())
    return arg + 1


pool = Pool(processes=4)

print '------------------------------------------------------------------------------------------'
result = pool.apply_async(worker, [1])
result.wait()
print result
print result.ready()
print result.get()
# ..........(worker start) [worker](pid:4105 ppid:4104)
# ..........(worker stop) [worker](pid:4105 ppid:4104)
# <multiprocessing.pool.ApplyResult object at 0x106c60590>
# True
# 2
print '------------------------------------------------------------------------------------------'
result = pool.map(worker, range(10))
print result
# ..........(worker start) [worker](pid:4005 ppid:4003)
# ..........(worker start) [worker](pid:4006 ppid:4003)
# ..........(worker start) [worker](pid:4004 ppid:4003)
# ..........(worker start) [worker](pid:4007 ppid:4003)
# ..........(worker stop) [worker](pid:4007 ppid:4003)
# ..........(worker start) [worker](pid:4007 ppid:4003)
# ..........(worker stop) [worker](pid:4007 ppid:4003)
# ..........(worker start) [worker](pid:4007 ppid:4003)
# ..........(worker stop) [worker](pid:4006 ppid:4003)
# ..........(worker start) [worker](pid:4006 ppid:4003)
# ..........(worker stop) [worker](pid:4006 ppid:4003)
# ..........(worker start) [worker](pid:4006 ppid:4003)
# ..........(worker stop) [worker](pid:4005 ppid:4003)
# ..........(worker start) [worker](pid:4005 ppid:4003)
# ..........(worker stop) [worker](pid:4004 ppid:4003)
# ..........(worker start) [worker](pid:4004 ppid:4003)
# ..........(worker stop) [worker](pid:4007 ppid:4003)
# ..........(worker stop) [worker](pid:4006 ppid:4003)
# ..........(worker stop) [worker](pid:4004 ppid:4003)
# ..........(worker stop) [worker](pid:4005 ppid:4003)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print '------------------------------------------------------------------------------------------'
result = pool.map_async(worker, range(10))
# ..........(worker start) [worker](pid:4091 ppid:4087)
# ..........(worker start) [worker](pid:4088 ppid:4087)
# ..........(worker start) [worker](pid:4089 ppid:4087)
# ..........(worker start) [worker](pid:4090 ppid:4087)
# ..........(worker stop) [worker](pid:4089 ppid:4087)
# ..........(worker start) [worker](pid:4089 ppid:4087)
# ..........(worker stop) [worker](pid:4091 ppid:4087)
# ..........(worker start) [worker](pid:4091 ppid:4087)
# ..........(worker stop) [worker](pid:4088 ppid:4087)
# ..........(worker start) [worker](pid:4088 ppid:4087)
# ..........(worker stop) [worker](pid:4090 ppid:4087)
# ..........(worker start) [worker](pid:4090 ppid:4087)
# ..........(worker stop) [worker](pid:4088 ppid:4087)
# ..........(worker start) [worker](pid:4088 ppid:4087)
# ..........(worker stop) [worker](pid:4091 ppid:4087)
# ..........(worker start) [worker](pid:4091 ppid:4087)
# ..........(worker stop) [worker](pid:4089 ppid:4087)
# ..........(worker stop) [worker](pid:4090 ppid:4087)
# ..........(worker stop) [worker](pid:4091 ppid:4087)
# ..........(worker stop) [worker](pid:4088 ppid:4087)
result.wait()
print result
print result.ready()
print result.get()
# <multiprocessing.pool.MapResult object at 0x106c60590>
# True
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print '------------------------------------------------------------------------------------------'
