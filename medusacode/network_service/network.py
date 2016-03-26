#!/usr/bin/env python
# coding:utf-8

"""
已经有如此多成熟优秀的框架（django，flask，pyramid），为什么要写 socket 程序 ？

不闻不若闻之，闻之不若见之，见之不若知之，知之不若行之。
I hear and I forget, I see and I remember, I do and I understand。
"""

"""
Distinction between sockets:

a “client” socket, is an endpoint of a conversation;
a “server” socket, is more like a switchboard operator.
The client application (your browser, for example) uses “client” sockets exclusively;
The web server uses both “server” sockets and “client” sockets.
"""

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

socket.connect(address)
    Connect to a remote socket at address.
    (The format of address depends on the address family.)

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
