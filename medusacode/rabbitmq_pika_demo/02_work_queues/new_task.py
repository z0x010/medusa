#!/usr/bin/env python
# coding:utf-8

import pika
import datetime

HOST = '192.168.100.100'
PORT = 5672
QUEUE_NAME = 'queue_test'

print '----------------------------------------------------------------------------------------------------'
connection = pika.BlockingConnection(
    parameters=pika.ConnectionParameters(
        host=HOST,
        port=PORT,
    )
)
print connection  # <pika.adapters.blocking_connection.BlockingConnection object at 0x109564b50>

channel = connection.channel(
    channel_number=None
)
print channel  # <pika.adapters.blocking_connection.BlockingChannel object at 0x1098355d0>

qd = channel.queue_declare(
    queue=QUEUE_NAME
)
print qd  # <METHOD(['channel_number=1', 'frame_type=1', "method=<Queue.DeclareOk(['consumer_count=0', 'message_count=0', 'queue=queue_test'])>"])>
print '----------------------------------------------------------------------------------------------------'
import random

message = random.randint(1, 5)
message = str(message)

bp = channel.basic_publish(
    exchange='',
    routing_key=QUEUE_NAME,
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,
    )
)
print bp  # True
print '[x] Sent: %s' % message

connection.close()
print '----------------------------------------------------------------------------------------------------'
