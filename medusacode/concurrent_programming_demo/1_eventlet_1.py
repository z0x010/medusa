#!/usr/bin/env python
# coding:utf-8

"""
eventlet 是基于 greenlet 实现的面向网络应用的并发处理框架，
提供线程池、队列等与其他 Python 线程、进程模型非常相似的 api，
并且提供了对 Python 发行版自带库及其他模块的超轻量并发适应性调整方法，
比直接使用 greenlet 要方便得多。
"""
"""
Eventlet is a concurrent networking library for Python that allows you to change how you run your code, not how you write it.
    It uses epoll or kqueue or libevent for highly scalable non-blocking I/O.
    Coroutines ensure that the developer uses a blocking style of programming that is similar to threading,
        but provide the benefits of non-blocking I/O.
    The event dispatch is implicit, which means you can easily use Eventlet from the Python interpreter,
        or as a small part of a larger application.
"""

import eventlet
from eventlet.green import socket

urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.so.com',
]

def work(url):
    return socket.gethostbyname(url)

"""
eventlet.spawn(func, *args, **kw)
    This launches a greenthread to call func.
    Spawning off multiple greenthreads gets work done in parallel.
    The return value from spawn is a greenthread.GreenThread object,
    which can be used to retrieve the return value of func.

GreenThread.wait()
    Returns the result of the main function of this GreenThread.
    If the result is a normal return value, wait() returns it.
    If it raised an exception, wait() will raise the same exception
        (though the stack trace will unavoidably contain some frames from within the greenthread module).
"""
jobs = [eventlet.spawn(socket.gethostbyname, url) for url in urls]
print jobs
# [<eventlet.greenthread.GreenThread object at 0x10c760e10>,
#  <eventlet.greenthread.GreenThread object at 0x10c760eb0>,
#  <eventlet.greenthread.GreenThread object at 0x10c760f50>]

print [job.wait() for job in jobs]
# ['61.135.169.125', '106.120.188.39', '111.206.81.174']
