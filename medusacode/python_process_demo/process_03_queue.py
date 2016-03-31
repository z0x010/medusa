#!/usr/bin/env python
# coding:utf-8

"""
Exchanging objects between processes
multiprocessing supports two types of communication channel between processes:
    Queues
    Pipes
"""
"""
Queue
    The Queue class is a near clone of Queue.Queue.
    Queues are thread and process safe.
"""
"""
class multiprocessing.Queue([maxsize])
    Returns a process shared queue implemented using a pipe and a few locks/semaphores.
    When a process first puts an item on the queue,
    a feeder thread is started which transfers objects from a buffer into the pipe.

    put(obj[, block[, timeout]])
        Put obj into the queue.
        If the optional argument block is True (the default) and timeout is None (the default),
        block if necessary until a free slot is available.
        If timeout is a positive number, it blocks at most timeout seconds and
        raises the Queue.Full exception if no free slot was available within that time.
        Otherwise (block is False), put an item on the queue if a free slot is immediately available,
        else raise the Queue.Full exception (timeout is ignored in that case).

    get([block[, timeout]])
        Remove and return an item from the queue.
        If optional args block is True (the default) and timeout is None (the default),
        block if necessary until an item is available.
        If timeout is a positive number, it blocks at most timeout seconds and
        raises the Queue.Empty exception if no item was available within that time.
        Otherwise (block is False), return an item if one is immediately available,
        else raise the Queue.Empty exception (timeout is ignored in that case).
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

def worker_produce(queue):
    print '..........(worker_produce start)'
    for n in range(5):
        time.sleep(random.random())
        item = random.randrange(0, 100, 1)
        queue.put(item)
        print '[worker_produce](pid:%s ppid:%s)' % (os.getpid(), os.getppid()), '+ produce item: %s' % item
    print '..........(worker_produce stop)'

def worker_consume(queue):
    print '..........(worker_consume start)'
    n = 0
    while n < 5:
        try:
            time.sleep(random.random())
            item = queue.get()
            print '[worker_consume](pid:%s ppid:%s)' % (os.getpid(), os.getppid()), '- consume item: %s' % item
            n += 1
        except QUEUE.Empty:
            time.sleep(random.random())
            continue
    print '..........(worker_consume stop)'


queue = Queue()
process_produce = Process(target=worker_produce, args=(queue,))
process_consume = Process(target=worker_consume, args=(queue,))
process_produce.start()
process_consume.start()
process_produce.join()
process_consume.join()

# ..........(worker_produce start)
# ..........(worker_consume start)
# [worker_produce](pid:1844 ppid:1843) + produce item: 7
# [worker_consume](pid:1845 ppid:1843) - consume item: 7
# [worker_produce](pid:1844 ppid:1843) + produce item: 28
# [worker_produce](pid:1844 ppid:1843) + produce item: 52
# [worker_consume](pid:1845 ppid:1843) - consume item: 28
# [worker_produce](pid:1844 ppid:1843) + produce item: 97
# [worker_consume](pid:1845 ppid:1843) - consume item: 52
# [worker_produce](pid:1844 ppid:1843) + produce item: 23
# ..........(worker_produce stop)
# [worker_consume](pid:1845 ppid:1843) - consume item: 97
# [worker_consume](pid:1845 ppid:1843) - consume item: 23
# ..........(worker_consume stop)
