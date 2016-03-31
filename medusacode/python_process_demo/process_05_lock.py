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
