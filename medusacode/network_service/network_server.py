#!/usr/bin/env python
# coding:utf-8

import socket

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
print 'listen %s %s' % (HOST, PORT)
while True:
    # accept
    client_connection, client_address = server_socket.accept()
    print 'accepted %s %s' % (client_connection, client_address)
    # recv
    data_received = client_connection.recv(4096)
    print 'received %s' % data_received
    # send
    data_send = '%s %s' % (data_received, '(from server)')
    client_connection.sendall(data_send)
    print 'sent %s' % data_send
    # close
    client_connection.close()
