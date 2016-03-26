#!/usr/bin/env python
# coding:utf-8

import socket

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
# send
data_send = 'hello there ~'
bytes_sent = client_socket.send(data_send)
print 'send %s %s bytes' % (data_send, bytes_sent)
# recv
data_received = client_socket.recv(4096)
print 'recv %s' % data_received
# close
client_socket.close()
