#!/usr/bin/env python
# coding:utf-8

"""
Lock Objects
    A primitive lock is a synchronization primitive that is not owned by a particular thread when locked.
    In Python, it is currently the lowest level synchronization primitive available,
    implemented directly by the thread extension module.

    A primitive lock is in one of two states, “locked” or “unlocked”.
    It is created in the unlocked state.
    It has two basic methods, acquire() and release().
    When the state is unlocked, acquire() changes the state to locked and returns immediately.
    When the state is locked, acquire() blocks until a call to release() in another thread changes it to unlocked,
    then the acquire() call resets it to locked and returns.
    The release() method should only be called in the locked state;
    it changes the state to unlocked and returns immediately.
    If an attempt is made to release an unlocked lock, a ThreadError will be raised.

    When more than one thread is blocked in acquire() waiting for the state to turn to unlocked,
    only one thread proceeds when a release() call resets the state to unlocked;
    which one of the waiting threads proceeds is not defined, and may vary across implementations.

    All methods are executed atomically.
"""
"""
multiprocessing contains equivalents of all the synchronization primitives from threading.

class multiprocessing.Lock
    A non-recursive lock object: a clone of threading.Lock.
class multiprocessing.RLock
    A recursive lock object: a clone of threading.RLock.

threading.Lock()
    A factory function that returns a new primitive lock object.
    Once a thread has acquired it, subsequent attempts to acquire it block, until it is released;
    any thread may release it.

    Lock.acquire([blocking])
        Acquire a lock, blocking or non-blocking.
        When invoked with the blocking argument set to True (the default), block until the lock is unlocked,
        then set it to locked and return True.
        When invoked with the blocking argument set to False, do not block.
        If a call with blocking set to True would block, return False immediately;
        otherwise, set the lock to locked and return True.

    Lock.release()
        Release a lock.
        When the lock is locked, reset it to unlocked, and return.
        If any other threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed.
        When invoked on an unlocked lock, a ThreadError is raised.
        There is no return value.

threading.RLock()
    A factory function that returns a new reentrant lock object.
    A reentrant lock must be released by the thread that acquired it.
    Once a thread has acquired a reentrant lock, the same thread may acquire it again without blocking;
    the thread must release it once for each time it has acquired it.

    RLock.acquire([blocking=1])
        Acquire a lock, blocking or non-blocking.
        When invoked without arguments:
            if this thread already owns the lock, increment the recursion level by one, and return immediately.
            Otherwise, if another thread owns the lock, block until the lock is unlocked.
            Once the lock is unlocked (not owned by any thread), then grab ownership,
            set the recursion level to one, and return.
            If more than one thread is blocked waiting until the lock is unlocked,
            only one at a time will be able to grab ownership of the lock.
            There is no return value in this case.
        When invoked with the blocking argument set to true,
            do the same thing as when called without arguments, and return true.
        When invoked with the blocking argument set to false,
            do not block.
            If a call without an argument would block, return false immediately;
            otherwise, do the same thing as when called without arguments, and return true.

    RLock.release()
        Release a lock, decrementing the recursion level.
        If after the decrement it is zero, reset the lock to unlocked (not owned by any thread),
        and if any other threads are blocked waiting for the lock to become unlocked,
        allow exactly one of them to proceed.
        If after the decrement the recursion level is still nonzero,
        the lock remains locked and owned by the calling thread.

        Only call this method when the calling thread owns the lock.
        A RuntimeError is raised if this method is called when the lock is unlocked.

        There is no return value.
"""

from multiprocessing import Process
from multiprocessing import Queue, Pipe
from multiprocessing import Lock, RLock, Event, Semaphore, Condition
from multiprocessing import Value, Array, Manager, Pool
import os
import time
import datetime
import random
import Queue as QUEUE

def worker(lock):
    lock.acquire()
    print '..........(worker%s start)' % os.getpid()
    time.sleep(0.5)
    for n in range(5):
        print '[worker](pid:%s ppid:%s)' % (os.getpid(), os.getppid()), '%s' % datetime.datetime.now()
        time.sleep(0.5)
    print '..........(worker%s stop)' % os.getpid()
    lock.release()


# [1] Lock: any thread may release it.
# lock = Lock()
# [2] RLock: must be released by the thread that acquired it.
lock = RLock()

for n in range(3):
    Process(target=worker, args=(lock,)).start()

# ..........(worker3036 start)
# [worker](pid:3036 ppid:3035) 2016-03-31 17:06:16.870674
# [worker](pid:3036 ppid:3035) 2016-03-31 17:06:17.371788
# [worker](pid:3036 ppid:3035) 2016-03-31 17:06:17.873000
# [worker](pid:3036 ppid:3035) 2016-03-31 17:06:18.373701
# [worker](pid:3036 ppid:3035) 2016-03-31 17:06:18.875097
# ..........(worker3036 stop)
# ..........(worker3037 start)
# [worker](pid:3037 ppid:3035) 2016-03-31 17:06:19.877859
# [worker](pid:3037 ppid:3035) 2016-03-31 17:06:20.379258
# [worker](pid:3037 ppid:3035) 2016-03-31 17:06:20.879533
# [worker](pid:3037 ppid:3035) 2016-03-31 17:06:21.380870
# [worker](pid:3037 ppid:3035) 2016-03-31 17:06:21.882137
# ..........(worker3037 stop)
# ..........(worker3038 start)
# [worker](pid:3038 ppid:3035) 2016-03-31 17:06:22.884874
# [worker](pid:3038 ppid:3035) 2016-03-31 17:06:23.385436
# [worker](pid:3038 ppid:3035) 2016-03-31 17:06:23.886247
# [worker](pid:3038 ppid:3035) 2016-03-31 17:06:24.386671
# [worker](pid:3038 ppid:3035) 2016-03-31 17:06:24.887104
# ..........(worker3038 stop)
