#!/usr/bin/env python
# coding:utf-8

"""
multiprocessing
"""

from multiprocessing import Process, Queue, Pipe, Lock, RLock, Value, Array, Manager, Pool
import os
import time
import datetime
import random
import Queue as QUEUE

print '----------------------------------------------------------------------------------------------------'
"""
In multiprocessing,
processes are spawned by creating a Process object and then calling its start() method.
Process follows the API of threading.Thread.
"""
# def info(title):
#     print title
#     print os.getpid(), os.getppid()
#
# def func(name):
#     info('func')
#     print 'hello', name
#
# info('main')
# process = Process(target=func, args=('Peter',))
# process.start()
# process.join()
print '----------------------------------------------------------------------------------------------------'
"""
Exchanging objects between processes

multiprocessing supports two types of communication channel between processes: Queues, Pipes
"""
print '----------------------------------------------------------------------------------------------------'
"""
[1] Queue
The Queue class is a near clone of Queue.Queue.
Queues are thread and process safe.
"""
# def f(q):
#     q.put('12345')
#
# q = Queue()
# p = Process(target=f, args=(q,))
# p.start()
# print q.get()
# p.join()
print '----------------------------------------------------------------------------------------------------'
"""
[2] Pipe
The Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex (two-way).
The two connection objects returned by Pipe() represent the two ends of the pipe.
Each connection object has send() and recv() methods (among others).
Note that data in a pipe may become corrupted if two processes (or threads) try to
read from or write to the same end of the pipe at the same time.
Of course there is no risk of corruption from processes using different ends of the pipe at the same time.
"""
# def f(conn):
#     conn.send('12345')
#     conn.close()
#
# parent_conn, child_conn = Pipe()
# p = Process(target=f, args=(child_conn,))
# p.start()
# print parent_conn.recv()
# p.join()
print '----------------------------------------------------------------------------------------------------'
"""
Synchronization between processes
"""
"""
multiprocessing contains equivalents of all the synchronization primitives from threading.
For instance one can use a lock to ensure that only one process prints to standard output at a time:
"""
# def f(l, i):
#     l.acquire()
#     print 'hello', i
#     l.release()
#
# lock = Lock()
# for n in range(10):
#     Process(target=f, args=(lock, n)).start()
#
# time.sleep(0.1)
print '----------------------------------------------------------------------------------------------------'
"""
Sharing state between processes
"""
"""
As mentioned above, when doing concurrent programming it is usually best to avoid using shared state as far as possible.
This is particularly true when using multiple processes.
However, if you really do need to use some shared data then multiprocessing provides a couple of ways of doing so.

[1] Shared memory
[2] Server process
"""
print '----------------------------------------------------------------------------------------------------'
"""
[1] Shared memory
Data can be stored in a shared memory map using Value or Array.
"""
# def f(v, a):
#     v.value = 321
#     for i in range(len(a)):
#         a[i] = -a[i]
#
# value = Value('d', 123)  # (C Type) double
# array = Array('i', range(10))  # (C Type) signed int
#
# process = Process(target=f, args=(value, array))
# process.start()
# process.join()
#
# print value.value
# print array[:]
print '----------------------------------------------------------------------------------------------------'
"""
[2] Server process
A manager object returned by Manager() controls a server process
which holds Python objects and allows other processes to manipulate them using proxies.

A manager returned by Manager() will support types:
list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Queue, Value, Array.

Server process managers are more flexible than using shared memory objects because
they can be made to support arbitrary object types.
Also, a single manager can be shared by processes on different computers over a network.
They are, however, slower than using shared memory.
"""
# def f(d, l):
#     d[1] = '1'
#     d['2'] = 2
#     d[3] = None
#     l.reverse()
#
# manager = Manager()
#
# d = manager.dict()
# l = manager.list(range(10))
#
# p = Process(target=f, args=(d, l))
# p.start()
# p.join()
#
# print d
# print l
print '----------------------------------------------------------------------------------------------------'
"""
Using a pool of workers
"""
"""
The Pool class represents a pool of worker processes.
It has methods which allows tasks to be offloaded to the worker processes in a few different ways.
"""
# def f(x):
#     return x*x
#
# pool = Pool(processes=4)
# result = pool.apply_async(f, [10])
#
# print result.get(timeout=1)
# print pool.map(f, range(10))
print '----------------------------------------------------------------------------------------------------'
