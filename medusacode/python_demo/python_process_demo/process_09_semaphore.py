#!/usr/bin/env python
# coding:utf-8

"""
A semaphore manages an internal counter
    which is decremented by each acquire() call,
    and incremented by each release() call.
The counter can never go below zero;
when acquire() finds that it is zero, it blocks, waiting until some other thread calls release().
"""
"""
class multiprocessing.Semaphore([value])
    A semaphore object: a clone of threading.Semaphore.

class threading.Semaphore([value])
    The optional argument gives the initial value for the internal counter;
    it defaults to 1. If the value given is less than 0, ValueError is raised.

    acquire([blocking])
        Acquire a semaphore.
        When invoked without arguments:
            if the internal counter is larger than zero on entry, decrement it by one and return immediately.
            If it is zero on entry, block, waiting until some other thread has called release() to make it larger than zero.
            This is done with proper interlocking so that if multiple acquire() calls are blocked,
            release() will wake exactly one of them up.
            The implementation may pick one at random,
            so the order in which blocked threads are awakened should not be relied on.
            There is no return value in this case.
        When invoked with blocking set to true,
            do the same thing as when called without arguments, and return true.
        When invoked with blocking set to false,
            do not block.
            If a call without an argument would block, return false immediately;
            otherwise, do the same thing as when called without arguments, and return true.

    release()
        Release a semaphore, incrementing the internal counter by one.
        When it was zero on entry and another thread is waiting for it to become larger than zero again,
        wake up that thread.
"""

from multiprocessing import Process, Queue, Pipe, Lock, RLock, Value, Array, Manager, Pool, Semaphore, Event
import multiprocessing
import os
import time
import datetime
import random
import Queue as QUEUE


def worker(semaphore):
    semaphore.acquire()
    print '========== %s acquired' % multiprocessing.current_process().name
    time.sleep(random.random())
    semaphore.release()
    print '========== %s released' % multiprocessing.current_process().name


semaphore = Semaphore(2)  # 最多只有2个进程可以获得 Semaphore

for n in range(5):
    Process(target=worker, args=(semaphore,)).start()

# ========== Process-1 acquired
# ========== Process-2 acquired
# ========== Process-2 released
# ========== Process-3 acquired
# ========== Process-1 released
# ========== Process-4 acquired
# ========== Process-3 released
# ========== Process-5 acquired
# ========== Process-4 released
# ========== Process-5 released
