#!/usr/bin/env python
# coding:utf-8

"""
socket.socket([family[, type[, proto]]])
    Create a new socket using the given address family, socket type and protocol number.
    The address family should be AF_INET (the default), AF_INET6 or AF_UNIX.
    The socket type should be SOCK_STREAM (the default), SOCK_DGRAM or perhaps one of the other SOCK_ constants.
    The protocol number is usually zero and may be omitted in that case.

socket.bind(address)
    Bind the socket to address.
    The socket must not already be bound.
    (The format of address depends on the address family.)

socket.listen(backlog)
    Listen for connections made to the socket.
    The backlog argument specifies the maximum number of queued connections and should be at least 0;
    the maximum value is system-dependent (usually 5), the minimum value is forced to 0.

socket.accept()
    Accept a connection.
    The socket must be bound to an address and listening for connections.
    The return value is a pair (conn, address)
    where conn is a new socket object usable to send and receive data on the connection,
    and address is the address bound to the socket on the other end of the connection.

socket.recv(bufsize[, flags])
    Receive data from the socket.
    The return value is a string representing the data received.
    The maximum amount of data to be received at once is specified by bufsize.
    See the Unix manual page recv(2) for the meaning of the optional argument flags; it defaults to zero.
    Note: For best match with hardware and network realities,
          the value of bufsize should be a relatively small power of 2, for example, 4096.

socket.send(string[, flags])
    Send data to the socket.
    The socket must be connected to a remote socket.
    The optional flags argument has the same meaning as for recv() above.
    Returns the number of bytes sent.
    Applications are responsible for checking that all data has been sent;
    if only some of the data was transmitted, the application needs to attempt delivery of the remaining data.

socket.sendall(string[, flags])
    Send data to the socket.
    The socket must be connected to a remote socket.
    The optional flags argument has the same meaning as for recv() above.
    Unlike send(), this method continues to send data from string until
    either all data has been sent or an error occurs.
    None is returned on success.
    On error, an exception is raised, and there is no way to determine how much data, if any, was successfully sent.

socket.close()
    Close the socket.
    All future operations on the socket object will fail.
    The remote end will receive no more data (after queued data is flushed).
    Sockets are automatically closed when they are garbage-collected.
    Note: close() releases the resource associated with a connection but does not necessarily
          close the connection immediately. If you want to close the connection in a timely fashion,
          call shutdown() before close().
"""

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
