#!/usr/bin/env python
# coding:utf-8

"""
Synchronization between processes
"""
"""
multiprocessing contains equivalents of all the synchronization primitives from threading.
"""
"""
class multiprocessing.Lock
    A non-recursive lock object: a clone of threading.Lock.
class multiprocessing.RLock
    A recursive lock object: a clone of threading.RLock.
threading.Lock()
    A factory function that returns a new primitive lock object.
    Once a thread has acquired it, subsequent attempts to acquire it block, until it is released;
    any thread may release it.
threading.RLock()
    A factory function that returns a new reentrant lock object.
    A reentrant lock must be released by the thread that acquired it.
    Once a thread has acquired a reentrant lock, the same thread may acquire it again without blocking;
    the thread must release it once for each time it has acquired it.
"""

from multiprocessing import Process, Queue, Pipe, Lock, RLock, Value, Array, Manager, Pool
import os
import time
import datetime
import random
import Queue as QUEUE

def worker(lock):
    print '..........(worker%s start)' % os.getpid()
    lock.acquire()
    time.sleep(0.5)
    for n in range(5):
        print '[worker](pid:%s ppid:%s)' % (os.getpid(), os.getppid()), '%s' % datetime.datetime.now()
        time.sleep(0.5)
    lock.release()
    print '..........(worker%s stop)' % os.getpid()


# [1] Lock: any thread may release it.
# lock = Lock()
# [2] RLock: must be released by the thread that acquired it.
lock = RLock()

for n in range(3):
    Process(target=worker, args=(lock,)).start()

# ..........(worker2166 start)
# ..........(worker2167 start)
# ..........(worker2168 start)
# [worker](pid:2166 ppid:2165) 2016-03-30 15:29:43.835243
# [worker](pid:2166 ppid:2165) 2016-03-30 15:29:44.335792
# [worker](pid:2166 ppid:2165) 2016-03-30 15:29:44.837087
# [worker](pid:2166 ppid:2165) 2016-03-30 15:29:45.338082
# [worker](pid:2166 ppid:2165) 2016-03-30 15:29:45.838882
# ..........(worker2166 stop)
# [worker](pid:2167 ppid:2165) 2016-03-30 15:29:46.840689
# [worker](pid:2167 ppid:2165) 2016-03-30 15:29:47.342065
# [worker](pid:2167 ppid:2165) 2016-03-30 15:29:47.843441
# [worker](pid:2167 ppid:2165) 2016-03-30 15:29:48.344760
# [worker](pid:2167 ppid:2165) 2016-03-30 15:29:48.845943
# ..........(worker2167 stop)
# [worker](pid:2168 ppid:2165) 2016-03-30 15:29:49.848822
# [worker](pid:2168 ppid:2165) 2016-03-30 15:29:50.349618
# [worker](pid:2168 ppid:2165) 2016-03-30 15:29:50.849982
# [worker](pid:2168 ppid:2165) 2016-03-30 15:29:51.351312
# [worker](pid:2168 ppid:2165) 2016-03-30 15:29:51.851715
# ..........(worker2168 stop)
