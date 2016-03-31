#!/usr/bin/env python
# coding:utf-8

"""
Event Objects
    This is one of the simplest mechanisms for communication between threads:
    one thread signals an event and other threads wait for it.

    An event object manages an internal flag
    that can be set to true with the set() method and reset to false with the clear() method.
    The wait() method blocks until the flag is true.
"""
"""
class multiprocessing.Event
    A clone of threading.Event.
    This method returns the state of the internal semaphore on exit,
    so it will always return True except if a timeout is given and the operation times out.

class threading.Event
    The internal flag is initially false.

    is_set()
    isSet()
        Return true if and only if the internal flag is true.
        Changed in version 2.6: Added is_set() spelling.
    set()
        Set the internal flag to true.
        All threads waiting for it to become true are awakened.
        Threads that call wait() once the flag is true will not block at all.
    clear()
        Reset the internal flag to false.
        Subsequently, threads calling wait() will block until set() is called to set the internal flag to true again.
    wait([timeout])
        Block until the internal flag is true.
        If the internal flag is true on entry, return immediately.
        Otherwise, block until another thread calls set() to set the flag to true,
        or until the optional timeout occurs.

        When the timeout argument is present and not None,
        it should be a floating point number specifying a timeout for the operation in seconds (or fractions thereof).

        This method returns the internal flag on exit,
        so it will always return True except if a timeout is given and the operation times out.
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


def worker(event):
    print '..........(worker start)', '[worker](pid:%s ppid:%s)' % (os.getpid(), os.getppid())
    time.sleep(random.random())
    event.wait()
    print '==========(internal flag is true)', '[worker](pid:%s ppid:%s)' % (os.getpid(), os.getppid())
    time.sleep(random.random())
    print '..........(worker stop)', '[worker](pid:%s ppid:%s)' % (os.getpid(), os.getppid())


event = Event()
print event.is_set()
# False

process_1 = Process(target=worker, args=(event,))
process_2 = Process(target=worker, args=(event,))
process_1.start()
process_2.start()
# ..........(worker start) [worker](pid:3058 ppid:3057)
# ..........(worker start) [worker](pid:3059 ppid:3057)

time.sleep(2)
event.set()
# ==========(internal flag is true) [worker](pid:3059 ppid:3057)
# ==========(internal flag is true) [worker](pid:3058 ppid:3057)
# ..........(worker stop) [worker](pid:3059 ppid:3057)
# ..........(worker stop) [worker](pid:3058 ppid:3057)

time.sleep(1)
print event.is_set()
# True
