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
GreenPool.imap(function, *iterables)
    This is the same as itertools.imap(), and has the same concurrency and memory behavior as starmap().
    It’s quite convenient for, e.g., farming out jobs from a file:
        def worker(line):
            return do_something(line)
        pool = GreenPool()
        for result in pool.imap(worker, open("filename", 'r')):
            print(result)
"""

greenpool = eventlet.GreenPool()
print [ret for ret in greenpool.imap(work, urls)]
# ['61.135.169.121', '106.38.241.48', '111.206.81.174']
