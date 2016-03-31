#!/usr/bin/env python
# coding:utf-8

"""
Condition Objects
    A condition variable is always associated with some kind of lock;
    this can be passed in or one will be created by default.
    (Passing one in is useful when several condition variables must share the same lock.)

    A condition variable has acquire() and release() methods that call the corresponding methods of the associated lock.
    It also has a wait() method, and notify() and notifyAll() methods.
    These three must only be called when the calling thread has acquired the lock, otherwise a RuntimeError is raised.

    The wait() method releases the lock, and then blocks until it is awakened
    by a notify() or notifyAll() call for the same condition variable in another thread.
    Once awakened, it re-acquires the lock and returns. It is also possible to specify a timeout.

    The notify() method wakes up one of the threads waiting for the condition variable, if any are waiting.
    The notifyAll() method wakes up all threads waiting for the condition variable.

    Note: the notify() and notifyAll() methods don’t release the lock;
    this means that the thread or threads awakened will not return from their wait() call immediately,
    but only when the thread that called notify() or notifyAll() finally relinquishes ownership of the lock.
"""
"""
class multiprocessing.Condition([lock])
    A condition variable: a clone of threading.Condition.
    If lock is specified then it should be a Lock or RLock object from multiprocessing.

class threading.Condition([lock])
    If the lock argument is given and not None,
    it must be a Lock or RLock object, and it is used as the underlying lock.
    Otherwise, a new RLock object is created and used as the underlying lock.

    acquire(*args)
        Acquire the underlying lock.
        This method calls the corresponding method on the underlying lock;
        the return value is whatever that method returns.

    release()
        Release the underlying lock.
        This method calls the corresponding method on the underlying lock;
        there is no return value.

    wait([timeout])
        Wait until notified or until a timeout occurs.
        If the calling thread has not acquired the lock when this method is called, a RuntimeError is raised.

        This method releases the underlying lock, and then blocks
        until it is awakened by a notify() or notifyAll() call for the same condition variable in another thread,
        or until the optional timeout occurs.
        Once awakened or timed out, it re-acquires the lock and returns.

        When the timeout argument is present and not None,
        it should be a floating point number specifying a timeout for the operation in seconds (or fractions thereof).

        When the underlying lock is an RLock, it is not released using its release() method,
        since this may not actually unlock the lock when it was acquired multiple times recursively.
        Instead, an internal interface of the RLock class is used,
        which really unlocks it even when it has been recursively acquired several times.
        Another internal interface is then used to restore the recursion level when the lock is reacquired.

    notify(n=1)
        By default, wake up one thread waiting on this condition, if any.
        If the calling thread has not acquired the lock when this method is called, a RuntimeError is raised.

        This method wakes up at most n of the threads waiting for the condition variable;
        it is a no-op if no threads are waiting.

        The current implementation wakes up exactly n threads, if at least n threads are waiting.
        However, it’s not safe to rely on this behavior.
        A future, optimized implementation may occasionally wake up more than n threads.

        Note: an awakened thread does not actually return from its wait() call until it can reacquire the lock.
        Since notify() does not release the lock, its caller should.

    notify_all()
    notifyAll()
        Wake up all threads waiting on this condition.
        This method acts like notify(), but wakes up all waiting threads instead of one.
        If the calling thread has not acquired the lock when this method is called, a RuntimeError is raised.
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


def worker_produce(condition, queue):
    print '..........(worker_produce start)'
    for n in range(5):
        time.sleep(random.random())
        condition.acquire()
        item = random.randrange(0, 100, 1)
        queue.put(item)
        print '[worker_produce](pid:%s ppid:%s)' % (os.getpid(), os.getppid()), '+ produce item: %s' % item
        condition.notify()
        condition.release()
    print '..........(worker_produce stop)'

def worker_consume(condition, queue):
    print '..........(worker_consume start)'
    for n in range(5):
        time.sleep(random.random())
        condition.acquire()
        while queue.empty():
            condition.wait()
        item = queue.get()
        print '[worker_consume](pid:%s ppid:%s)' % (os.getpid(), os.getppid()), '- consume item: %s' % item
        condition.release()
    print '..........(worker_consume stop)'


lock = RLock()
condition = Condition(lock)

queue = Queue()

process_produce = Process(target=worker_produce, args=(condition, queue))
process_consume = Process(target=worker_consume, args=(condition, queue))
process_produce.start()
process_consume.start()
process_produce.join()
process_consume.join()

# ..........(worker_produce start)
# ..........(worker_consume start)
# [worker_produce](pid:3140 ppid:3139) + produce item: 76
# [worker_consume](pid:3141 ppid:3139) - consume item: 76
# [worker_produce](pid:3140 ppid:3139) + produce item: 6
# [worker_consume](pid:3141 ppid:3139) - consume item: 6
# [worker_produce](pid:3140 ppid:3139) + produce item: 26
# [worker_consume](pid:3141 ppid:3139) - consume item: 26
# [worker_produce](pid:3140 ppid:3139) + produce item: 24
# [worker_produce](pid:3140 ppid:3139) + produce item: 9
# ..........(worker_produce stop)
# [worker_consume](pid:3141 ppid:3139) - consume item: 24
# [worker_consume](pid:3141 ppid:3139) - consume item: 9
# ..........(worker_consume stop)
