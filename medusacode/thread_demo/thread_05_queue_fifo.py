#!/usr/bin/env python
# coding=utf-8

"""
The Queue module implements multi-producer, multi-consumer queues.
It is especially useful in threaded programming when information must be exchanged safely between multiple threads.
The Queue class in this module implements all the required locking semantics.

The module implements three types of queue, which differ only in the order in which the entries are retrieved.
In a FIFO queue, the first tasks added are the first retrieved.
In a LIFO queue, the most recently added entry is the first retrieved (operating like a stack).
With a priority queue, the entries are kept sorted (using the heapq module) and the lowest valued entry is retrieved first.
"""

import time
import datetime
import thread
import threading
import Queue
import random


class MyThread(threading.Thread):
    def __init__(self, thread_id, thread_name, queue):
        threading.Thread.__init__(self)  # 需要调用父类的构造函数
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.queue = queue
        pass
    def __del__(self):
        pass
    pass

class WriteThread(MyThread):
    def run(self):
        print '[%s][%s]=====[start]' % (self.thread_id, self.thread_name)
        for n in range(10):
            time.sleep(random.random())
            write(self.queue)
            pass
        print '[%s][%s]=====[stop]' % (self.thread_id, self.thread_name)
        pass
    pass

class ReadThread(MyThread):
    def run(self):
        print '[%s][%s]=====[start]' % (self.thread_id, self.thread_name)
        for n in range(10):
            time.sleep(2*random.random())
            read(self.queue)
            pass
        print '[%s][%s]=====[stop]' % (self.thread_id, self.thread_name)
        pass
    pass

def write(queue):
    item = random.randrange(0, 100, 1)
    queue.put(item)
    print "[+][write]", item, "[Size]", queue.qsize()
    pass

def read(queue):
    item = queue.get()
    print "[-][read]", item, "[Size]", queue.qsize()
    pass

def main():
    thread_queue = Queue.Queue()
    th1 = WriteThread('1', "Thread-1", thread_queue)
    th2 = ReadThread('2', "Thread-2", thread_queue)
    th1.start()
    th2.start()
    th1.join()  # 等待线程结束
    th2.join()  # 等待线程结束
    return

if __name__ == "__main__":
    main()
