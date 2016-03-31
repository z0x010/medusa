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
[2] Server process
    Managers provide a way to create data which can be shared between different processes.
    A manager object controls a server process which manages shared objects.
    Other processes can access the shared objects by using proxies.

    A manager object returned by Manager() controls a server process
    which holds Python objects and allows other processes to manipulate them using proxies.
    A manager returned by Manager() will support types:
    list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Queue, Value, Array.
    Server process managers are more flexible than using shared memory objects because
    they can be made to support arbitrary object types.
    Also, a single manager can be shared by processes on different computers over a network.
    They are, however, slower than using shared memory.
"""
"""
multiprocessing.Manager()
    Returns a started SyncManager object which can be used for sharing objects between processes.
    The returned manager object corresponds to a spawned child process and
    has methods which will create shared objects and return corresponding proxies.
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

def worker(l, d, lock):
    lock.acquire()
    print '..........(worker start)', '[worker](pid:%s ppid:%s)' % (os.getpid(), os.getppid())
    l.append(random.randrange(0, 100, 1))
    d.update({random.choice('abcdefghijklmnopqrstuvwxyz'): random.randrange(0, 100, 1)})
    print l
    print d
    print '..........(worker stop)', '[worker](pid:%s ppid:%s)' % (os.getpid(), os.getppid())
    lock.release()


manager = Manager()
proxy_list = manager.list([])
proxy_dict = manager.dict({})
lock = RLock()

process_1 = Process(target=worker, args=(proxy_list, proxy_dict, lock))
process_2 = Process(target=worker, args=(proxy_list, proxy_dict, lock))
process_1.start()
process_2.start()
process_1.join()
process_2.join()
# ..........(worker start) [worker](pid:3222 ppid:3220)
# [69]
# {'u': 82}
# ..........(worker stop) [worker](pid:3222 ppid:3220)
# ..........(worker start) [worker](pid:3223 ppid:3220)
# [69, 22]
# {'r': 79, 'u': 82}
# ..........(worker stop) [worker](pid:3223 ppid:3220)

print proxy_list
print proxy_dict
# [13, 44]
# {'l': 52, 'v': 88}
