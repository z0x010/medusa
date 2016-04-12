#!/usr/bin/env python
# coding:utf-8

"""
串行执行
"""

# from gevent import monkey; monkey.patch_all()
import gevent
import urllib2
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

# [process: 20764][thread: 140735181955840] GET: http://www.baidu.com
# [process: 20764][thread: 140735181955840] received 98264 bytes from http://www.baidu.com
# [process: 20764][thread: 140735181955840] GET: http://www.sogou.com
# [process: 20764][thread: 140735181955840] received 14887 bytes from http://www.sogou.com
# [process: 20764][thread: 140735181955840] GET: http://www.so.com
# [process: 20764][thread: 140735181955840] received 198036 bytes from http://www.so.com
