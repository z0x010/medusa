#!/usr/bin/env python
# coding:utf-8

import gevent
import datetime
import os

def work():
    print os.getpid(), datetime.datetime.now()

jobs = [gevent.spawn(work) for _ in range(3)]
# 19669 2016-04-12 17:14:02.728888
# 19669 2016-04-12 17:14:02.728917
# 19669 2016-04-12 17:14:02.728930

gevent.joinall(jobs, timeout=3)

print [job.value for job in jobs]
