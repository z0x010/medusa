#!/usr/bin/env python
# coding:utf-8

"""
In multiprocessing,
processes are spawned by creating a Process object and then calling its start() method.
(Process follows the API of threading.Thread)
"""
"""
class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={})
    Process objects represent activity that is run in a separate process.
    The Process class has equivalents of all the methods of threading.Thread.
    The constructor should always be called with keyword arguments:
        group should always be None; it exists solely for compatibility with threading.Thread.
        target is the callable object to be invoked by the run() method. It defaults to None, meaning nothing is called.
        name is the process name. By default, a unique name is constructed of the form ‘Process-N1:N2:...:Nk‘.
        args is the argument tuple for the target invocation.
        kwargs is a dictionary of keyword arguments for the target invocation.
        By default, no arguments are passed to target.
"""

from multiprocessing import Process, Queue, Pipe, Lock, Value, Array, Manager, Pool
import os
import time
import datetime

def worker():
    print '..........(worker start)'
    for n in range(5):
        print '[worker](pid:%s ppid:%s)' % (os.getpid(), os.getppid()), '%s' % datetime.datetime.now()
        time.sleep(0.5)
    print '..........(worker stop)'


print '..........(main start)'
process = Process(target=worker, args=(), kwargs={})
print '[main](pid:%s ppid:%s)' % (os.getpid(), os.getppid())
process.start()
process.join()
print '..........(main stop)'

# ..........(main start)
# [main](pid:6400 ppid:536)
# ..........(worker start)
# [worker](pid:6401 ppid:6400) 2016-03-29 20:13:58.290350
# [worker](pid:6401 ppid:6400) 2016-03-29 20:13:58.791528
# [worker](pid:6401 ppid:6400) 2016-03-29 20:13:59.292803
# [worker](pid:6401 ppid:6400) 2016-03-29 20:13:59.793247
# [worker](pid:6401 ppid:6400) 2016-03-29 20:14:00.293693
# ..........(worker stop)
# ..........(main stop)
