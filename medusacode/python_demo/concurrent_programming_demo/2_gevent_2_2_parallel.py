#!/usr/bin/env python
# coding:utf-8

"""
并行执行
"""

"""
Monkey patching

The example above used gevent.socket for socket operations.
If the standard socket module was used the example would have taken 3 times longer to complete
because the DNS requests would be sequential (serialized).
Using the standard socket module inside greenlets makes gevent rather pointless,
so what about existing modules and packages that are built on top of socket
(including the standard library modules like urllib)?

That’s where monkey patching comes in.
The functions in gevent.monkey carefully replace functions and classes
in the standard socket module with their cooperative counterparts.
That way even the modules that are unaware of gevent can benefit from running in a multi-greenlet environment.
"""

from gevent import monkey; monkey.patch_all()
import gevent
import urllib2  # it's usable from multiple greenlets now
import os
import thread

urls = [
    'http://www.baidu.com',
    'http://www.sogou.com',
    'http://www.so.com',
]

def work(url):
    print '[process: %s][thread: %s] GET: %s' % (os.getpid(), thread.get_ident(), url)
    ret = urllib2.urlopen(url).read()
    print '[process: %s][thread: %s] received %s bytes from %s' % (os.getpid(), thread.get_ident(), len(ret), url)

gevent.joinall([
    gevent.spawn(work, urls[0]),
    gevent.spawn(work, urls[1]),
    gevent.spawn(work, urls[2]),
])

# [process: 20775][thread: 4322480528] GET: http://www.baidu.com
# [process: 20775][thread: 4323812528] GET: http://www.sogou.com
# [process: 20775][thread: 4323812688] GET: http://www.so.com
# [process: 20775][thread: 4322480528] received 98010 bytes from http://www.baidu.com
# [process: 20775][thread: 4323812528] received 14887 bytes from http://www.sogou.com
# [process: 20775][thread: 4323812688] received 198036 bytes from http://www.so.com
