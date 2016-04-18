#!/usr/bin/env python
# coding:utf-8

import pika
import datetime

HOST = '192.168.100.100'
PORT = 5672
QUEUE_NAME = 'task_queue'

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

"""
When RabbitMQ quits or crashes it will forget the queues and messages unless you tell it not to.
Two things are required to make sure that messages aren't lost:
we need to mark both the queue and messages as durable.
"""
qd = channel.queue_declare(
    queue=QUEUE_NAME,
    durable=True,  # make the queue durable (survive reboots of the broker)
)
print qd  # <METHOD(['channel_number=1', 'frame_type=1', "method=<Queue.DeclareOk(['consumer_count=0', 'message_count=0', 'queue=queue_test'])>"])>
print '----------------------------------------------------------------------------------------------------'
import random

message = random.randint(1, 5)
message = str(message)

"""
Mark our messages as persistent - by supplying a delivery_mode property with a value of 2
"""
bp = channel.basic_publish(
    exchange='',
    routing_key=QUEUE_NAME,
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    )
)
print bp  # True
print '[x] Sent: %s' % message

connection.close()
print '----------------------------------------------------------------------------------------------------'
