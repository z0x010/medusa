#!/usr/bin/env python
# coding=utf-8

"""
 class threading.Thread(group=None, target=None, name=None, args=(), kwargs={})
    This constructor should always be called with keyword arguments. Arguments are:
    group should be None; reserved for future extension when a ThreadGroup class is implemented.
    target is the callable object to be invoked by the run() method. Defaults to None, meaning nothing is called.
    name is the thread name. By default, a unique name is constructed of the form “Thread-N” where N is a small decimal number.
    args is the argument tuple for the target invocation. Defaults to ().
    kwargs is a dictionary of keyword arguments for the target invocation. Defaults to {}.
    If the subclass overrides the constructor,
    it must make sure to invoke the base class constructor (Thread.__init__()) before doing anything else to the thread.
"""

import time
import datetime
import thread
import threading

class MyThread(threading.Thread):
    def __init__(self, thread_id, thread_name, count):
        threading.Thread.__init__(self)  # 需要调用父类的构造函数
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.count = count
        pass
    def __del__(self):
        pass
    def run(self):
        print '[%s][%s]=====[start]' % (self.thread_id, self.thread_name)
        print_datetime(self.thread_name, 0.5, self.count)
        print '[%s][%s]=====[stop]' % (self.thread_id, self.thread_name)
        return True
    pass

def print_datetime(thread_name, delay, count):
    c = 0
    while c < count:
        time.sleep(delay)
        c += 1
        print '[%s][%s]' % (thread_name, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        pass
    return True

def main():
    th1 = MyThread('1', "Thread-1", 3)
    th2 = MyThread('2', "Thread-2", 5)
    th1.start()
    th2.start()
    th1.join()  # 等待线程结束
    th2.join()  # 等待线程结束
    return

if __name__ == "__main__":
    main()
