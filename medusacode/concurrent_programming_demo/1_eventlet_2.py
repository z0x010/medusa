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
GreenPool.spawn(function, *args, **kwargs)
    Run the function with its arguments in its own green thread.
        Returns the GreenThread object that is running the function, which can be used to retrieve the results.
    If the pool is currently at capacity,
        spawn will block until one of the running greenthreads completes its task and frees up a slot.
    This function is reentrant;
        function can call spawn on the same pool without risk of deadlocking the whole thing.

GreenPool.waitall()
    Waits until all greenthreads in the pool are finished working.

"""

greenpool = eventlet.GreenPool()

jobs = [greenpool.spawn(work, url) for url in urls]
print jobs
# [<eventlet.greenthread.GreenThread object at 0x10c060eb0>,
#  <eventlet.greenthread.GreenThread object at 0x10c060f50>,
#  <eventlet.greenthread.GreenThread object at 0x10c19b050>]

greenpool.waitall()
print [job.wait() for job in jobs]
# ['180.149.131.98', '106.38.241.48', '106.120.160.134']
