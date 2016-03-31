#!/usr/bin/env python
# coding:utf-8

import socket
import datetime

HOST = '127.0.0.1'
PORT = 9999


# socket
client_socket = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM,
)

# connect
client_socket.connect(
    (HOST, PORT)
)

# client_socket.getsockname()
# ('127.0.0.1', 54060)

# send
data_send = 'hello there ~'
bytes_sent = client_socket.send(data_send)
print '[%s](sent) %s %s bytes' % (datetime.datetime.now(), data_send, bytes_sent)

# recv
data_received = client_socket.recv(4096)
print '[%s](received) %s' % (datetime.datetime.now(), data_received)

# close
client_socket.close()
