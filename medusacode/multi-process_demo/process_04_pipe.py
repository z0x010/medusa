#!/usr/bin/env python
# coding:utf-8

"""
Exchanging objects between processes
multiprocessing supports two types of communication channel between processes:
    Queues
    Pipes
"""
"""
Pipe
    The Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex (two-way).
Connection
    Connection objects allow the sending and receiving of picklable objects or strings.
    They can be thought of as message oriented connected sockets.
    Connection objects are usually created using Pipe().
"""
"""
multiprocessing.Pipe([duplex])
    Returns a pair (conn1, conn2) of Connection objects representing the ends of a pipe.
    If duplex is True (the default) then the pipe is bidirectional.
    If duplex is False then the pipe is unidirectional:
        conn1 can only be used for receiving messages
        conn2 can only be used for sending messages.

class multiprocessing.Connection
    send(obj)
        Send an object to the other end of the connection which should be read using recv().
        The object must be picklable.
        Very large pickles may raise a ValueError exception.
    recv()
        Return an object sent from the other end of the connection using send().
        Blocks until there is something to receive.
        Raises EOFError if there is nothing left to receive and the other end was closed.
"""

from multiprocessing import Process, Queue, Pipe, Lock, Value, Array, Manager, Pool
import os
import time
import datetime
import random
import Queue as QUEUE

def worker_produce(pipe):
    for n in range(5):
        item = random.randrange(0, 100, 1)
        pipe.send(item)
        print '[worker_produce](pid:%s ppid:%s)' % (os.getpid(), os.getppid()), '+ produce item: %s' % item
        time.sleep(random.random())

def worker_consume(pipe):
    for n in range(5):
        item = pipe.recv()
        print '[worker_consume](pid:%s ppid:%s)' % (os.getpid(), os.getppid()), '- consume item: %s' % item
        time.sleep(random.random())


pipe_1, pipe_2 = Pipe()
process_produce = Process(target=worker_produce, args=(pipe_1,))
process_consume = Process(target=worker_consume, args=(pipe_2,))
process_produce.start()
process_consume.start()
process_produce.join()
process_consume.join()

# [worker_produce](pid:7214 ppid:7213) + produce item: 96
# [worker_consume](pid:7215 ppid:7213) - consume item: 96
# [worker_produce](pid:7214 ppid:7213) + produce item: 18
# [worker_produce](pid:7214 ppid:7213) + produce item: 58
# [worker_consume](pid:7215 ppid:7213) - consume item: 18
# [worker_produce](pid:7214 ppid:7213) + produce item: 60
# [worker_consume](pid:7215 ppid:7213) - consume item: 58
# [worker_produce](pid:7214 ppid:7213) + produce item: 41
# [worker_consume](pid:7215 ppid:7213) - consume item: 60
# [worker_consume](pid:7215 ppid:7213) - consume item: 41
