#!/usr/bin/env python
# coding:utf-8

"""
gevent 是一个基于协程（coroutine）的 Python 网络函数库，通过使用 greenlet 提供了一个在 libev 事件循环顶部的高级别并发API。
"""
"""
gevent is a coroutine-based Python networking library
that uses greenlet to provide a high-level synchronous API on top of the libev event loop.

Features include:
    Fast event loop based on libev (epoll on Linux, kqueue on FreeBSD).
    Lightweight execution units based on greenlet.
    API that re-uses concepts from the Python standard library (for example there are gevent.event.Events and gevent.queue.Queues).
    Cooperative sockets with SSL support
    DNS queries performed through threadpool or c-ares.
    Monkey patching utility to get 3rd party modules to become cooperative

gevent is inspired by eventlet but features more consistent API, simpler implementation and better performance.
"""
"""
Python 通过 yield 提供了对协程的基本支持，但是不完全。而第三方的 gevent 为 Python 提供了比较完善的协程支持。

gevent 是第三方库，通过 greenlet 实现协程，其基本思想是：
    当一个 greenlet 遇到IO操作时，比如访问网络，就自动切换到其他的 greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。
    由于IO操作非常耗时，经常使程序处于等待状态，有了 gevent 为我们自动切换协程，就保证总有 greenlet 在运行，而不是等待IO。

由于切换是在IO操作时自动完成，所以 gevent 需要修改 Python 自带的一些标准库，这一过程在启动时通过 monkey patch 完成。
"""

import gevent
from gevent import socket

urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.so.com',
]

"""
gevent.spawn(function, *args, **kwargs)
    Create a new Greenlet object and schedule it to run function(*args, **kwargs).
    This can be used as gevent.spawn or Greenlet.spawn.
    The arguments are passed to Greenlet.__init__().

gevent.joinall(greenlets, timeout=None, raise_error=False, count=None)
    Wait for the greenlets to finish.
    Parameters:
        greenlets – A sequence (supporting len()) of greenlets to wait for.
        timeout (float) – If given, the maximum number of seconds to wait.
    Returns:
        A sequence of the greenlets that finished before the timeout (if any) expired.

Greenlet.value
    Holds the value returned by the function if the greenlet has finished successfully.
    Until then, or if it finished in error, None.
"""

"""
The gevent.socket.gethostbyname() function has the same interface as the standard socket.gethostbyname()
but it does not block the whole interpreter and thus lets the other greenlets proceed with their requests unhindered.
"""
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
print jobs
# [<Greenlet at 0x104d5fcd0: gethostbyname('www.baidu.com')>,
#  <Greenlet at 0x104d5f9b0: gethostbyname('www.sogou.com')>,
#  <Greenlet at 0x104d5fd70: gethostbyname('www.so.com')>]
"""
After the jobs have been spawned, gevent.joinall() waits for them to complete, allowing up to (timeout) seconds.
"""
greenlets = gevent.joinall(jobs, timeout=3)
print greenlets
# [<Greenlet at 0x104d5fcd0: gethostbyname('www.baidu.com')>,
#  <Greenlet at 0x104d5f9b0: gethostbyname('www.sogou.com')>,
#  <Greenlet at 0x104d5fd70: gethostbyname('www.so.com')>]
"""
The results are then collected by checking the value property.
"""
print [job.value for job in jobs]
# ['61.135.169.125', '123.126.113.46', '111.206.81.174']
