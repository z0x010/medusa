#!/usr/bin/env python
# coding:utf-8

import redis

"""
class redis.StrictRedis(
    host='localhost',
    port=6379, db=0,
    password=None,
    socket_timeout=None,
    connection_pool=None,
    charset='utf-8',
    errors='strict',
    unix_socket_path=None)

    Implementation of the Redis protocol.
    This abstract class provides a Python interface to all Redis commands and an implementation of the Redis protocol.
    Connection and Pipeline derive from this, implementing how the commands are sent and received to the Redis server.
"""

redis_db = redis.StrictRedis(
    host='192.168.100.100',
    port=6379,
    db=0,
)

# print id(redis_db)
# # 4380281360
# print redis_db.set('k_123', 'v_123')
# # True
# print redis_db.get('k_123')
# # v_123

"""
Python的模块(module)，就是最 pythonic 的 singleton 典范。
模块在在一个应用程序中只有一份，它本身就是单例的。
所以只要将所需要的属性和方法，直接暴露在模块中变成模块的全局变量和全局方法即可！
"""
