#!/usr/bin/env python
# coding:utf-8

"""
In multiprocessing,
processes are spawned by creating a Process object and then calling its start() method.
(Process follows the API of threading.Thread)
"""

from multiprocessing import Process
from multiprocessing import Queue, Pipe
from multiprocessing import Lock, RLock, Event, Semaphore, Condition
from multiprocessing import Value, Array, Manager, Pool
import os
import time
import datetime

class MyProcess(Process):
    def __init__(self):
        Process.__init__(self)
    def run(self):
        print '..........(worker start)'
        for n in range(5):
            print '[worker](pid:%s ppid:%s)' % (os.getpid(), os.getppid()), '%s' % datetime.datetime.now()
            time.sleep(0.5)
        print '..........(worker stop)'


print '..........(main start)'
process = MyProcess()
print '[main](pid:%s ppid:%s)' % (os.getpid(), os.getppid())
process.start()
process.join()
print '..........(main stop)'

# ..........(main start)
# [main](pid:6490 ppid:536)
# ..........(worker start)
# [worker](pid:6491 ppid:6490) 2016-03-29 20:18:32.468724
# [worker](pid:6491 ppid:6490) 2016-03-29 20:18:32.969163
# [worker](pid:6491 ppid:6490) 2016-03-29 20:18:33.470393
# [worker](pid:6491 ppid:6490) 2016-03-29 20:18:33.970710
# [worker](pid:6491 ppid:6490) 2016-03-29 20:18:34.471355
# ..........(worker stop)
# ..........(main stop)
