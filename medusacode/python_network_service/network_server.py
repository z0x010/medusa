#!/usr/bin/env python
# coding:utf-8

import socket
import datetime

HOST = '127.0.0.1'
PORT = 9999


# socket
server_socket = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM,
)

# bind
server_socket.bind(
    (HOST, PORT)
)

# listen
server_socket.listen(
    1,
)
print '[%s](listen) %s %s' % (datetime.datetime.now(), HOST, PORT)

while True:
    # accept
    client_connection, client_address = server_socket.accept()
    print '[%s](accepted) %s %s' % (datetime.datetime.now(), client_connection, client_address)

    # recv
    data_received = client_connection.recv(4096)
    print '[%s](received) %s' % (datetime.datetime.now(), data_received)

    # send
    data_send = 'server time: %s' % datetime.datetime.now()
    client_connection.sendall(data_send)
    print '[%s](sent) %s' % (datetime.datetime.now(), data_send)

    # close
    client_connection.close()
