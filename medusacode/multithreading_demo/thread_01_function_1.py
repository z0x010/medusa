#!/usr/bin/env python
# coding=utf-8

"""
thread.start_new_thread(function, args[, kwargs])
    Start a new thread and return its identifier.
    The thread executes the function function with the argument list args (which must be a tuple).
    The optional kwargs argument specifies a dictionary of keyword arguments.
    When the function returns, the thread silently exits.
    When the function terminates with an unhandled exception,
    a stack trace is printed and then the thread exits (but other threads continue to run).
"""

import time
import datetime
import thread

def print_datetime(thread_name, delay, count):
    c = 0
    while c < count:
        time.sleep(delay)
        c += 1
        print '[%s][%s]' % (thread_name, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        pass
    return True

def main():
    try:
        thread_id_1 = thread.start_new_thread(print_datetime, ('Thread-1', 0.5, 3))
        thread_id_2 = thread.start_new_thread(print_datetime, ('Thread-2', 0.5, 5))
    except Exception, e:
        print e
        pass
    # 如果不加死循环，则子线程创建后就会随着主线程的退出而被关闭
    # 线程同步，目的是让主线程等待子线程结束后再继续运行
    while True:
        pass
    return

if __name__ == "__main__":
    main()
