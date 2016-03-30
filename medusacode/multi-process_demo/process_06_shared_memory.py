#!/usr/bin/env python
# coding:utf-8

"""
Sharing state between processes
"""
"""
When doing concurrent programming it is usually best to avoid using shared state as far as possible.
This is particularly true when using multiple processes.
However, if you really do need to use some shared data then multiprocessing provides a couple of ways of doing so.
    [1] Shared memory
    [2] Server process
"""
"""
[1] Shared memory
    Data can be stored in a shared memory map using Value or Array.
"""
"""
multiprocessing.Value(typecode_or_type, *args[, lock])
    Return a ctypes object allocated from shared memory.
    By default the return value is actually a synchronized wrapper for the object.

    typecode_or_type determines the type of the returned object:
    it is either a ctypes type or a one character typecode of the kind used by the array module.
    *args is passed on to the constructor for the type.
    If lock is True (the default) then a new recursive lock object is created to synchronize access to the value.
    If lock is a Lock or RLock object then that will be used to synchronize access to the value.
    If lock is False then access to the returned object will not be automatically protected by a lock,
    so it will not necessarily be “process-safe”.

multiprocessing.Array(typecode_or_type, size_or_initializer, *, lock=True)
    Return a ctypes array allocated from shared memory.
    By default the return value is actually a synchronized wrapper for the array.

    typecode_or_type determines the type of the elements of the returned array:
    it is either a ctypes type or a one character typecode of the kind used by the array module.
    If size_or_initializer is an integer, then it determines the length of the array,
    and the array will be initially zeroed. Otherwise, size_or_initializer is a sequence which is used to
    initialize the array and whose length determines the length of the array.
    If lock is True (the default) then a new lock object is created to synchronize access to the value.
    If lock is a Lock or RLock object then that will be used to synchronize access to the value.
    If lock is False then access to the returned object will not be automatically protected by a lock,
    so it will not necessarily be “process-safe”.

ctypes — A foreign function library for Python
    ctypes is a foreign function library for Python.
    It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
    It can be used to wrap these libraries in pure Python.
"""

from multiprocessing import Process, Queue, Pipe, Lock, RLock, Value, Array, Manager, Pool
import os
import time
import datetime
import random
import Queue as QUEUE

def worker(value, array):
    print '..........(worker start)', '[worker](pid:%s ppid:%s)' % (os.getpid(), os.getppid())
    time.sleep(random.random())
    value.value += 0.1
    for n in range(len(array)):
        array[n] *= 2
    print value.value
    print array[:]
    print '..........(worker stop)', '[worker](pid:%s ppid:%s)' % (os.getpid(), os.getppid())


value = Value('d', 1.0)  # (C Type) double
array = Array('i', range(10))  # (C Type) signed int

process_1 = Process(target=worker, args=(value, array))
process_2 = Process(target=worker, args=(value, array))
process_1.start()
process_2.start()
process_1.join()
process_2.join()
# ..........(worker start) [worker](pid:3095 ppid:3094)
# ..........(worker start) [worker](pid:3096 ppid:3094)
# 1.1
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# ..........(worker stop) [worker](pid:3096 ppid:3094)
# 1.2
# [0, 4, 8, 12, 16, 20, 24, 28, 32, 36]
# ..........(worker stop) [worker](pid:3095 ppid:3094)

print value
print value.value
# <Synchronized wrapper for c_double(1.2000000000000002)>
# 1.2
print array
print array[:]
# <SynchronizedArray wrapper for <multiprocessing.sharedctypes.c_int_Array_10 object at 0x104df9b90>>
# [0, 4, 8, 12, 16, 20, 24, 28, 32, 36]
