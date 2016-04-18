#!/usr/bin/env python
# coding:utf-8

import pika
import datetime
import time

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

qd = channel.queue_declare(
    queue=QUEUE_NAME,
    durable=True,  # make the queue durable (survive reboots of the broker)
)
print qd  # <METHOD(['channel_number=1', 'frame_type=1', "method=<Queue.DeclareOk(['consumer_count=0', 'message_count=0', 'queue=queue_test'])>"])>
print '----------------------------------------------------------------------------------------------------'
"""
In order to make sure a message is never lost, RabbitMQ supports message acknowledgments.
An ack(nowledgement) is sent back from the consumer to tell RabbitMQ
that a particular message had been received, processed and that RabbitMQ is free to delete it.

If a consumer dies (its channel is closed, connection is closed, or TCP connection is lost) without sending an ack,
RabbitMQ will understand that a message wasn't processed fully and will re-queue it.
If there are other consumers online at the same time, it will then quickly redeliver it to another consumer.
That way you can be sure that no message is lost, even if the workers occasionally die.

There aren't any message timeouts; RabbitMQ will redeliver the message when the consumer dies.
It's fine even if processing a message takes a very, very long time.
"""

def callback(ch, method, properties, body):
    print('[x] Received: %s' % body)
    for n in range(int(body)):
        time.sleep(1)
        print '[*] work: %s %s' % (n+1, '.' * (n+1))
    print '[x] Done'
    ch.basic_ack(delivery_tag=method.delivery_tag)  # An ack(nowledgement) is sent back from the consumer to tell the broker(RabbitMQ)

"""
Use the basic.qos method with the prefetch_count=1 setting.
This tells RabbitMQ not to give more than one message to a worker at a time.
Or, in other words, don't dispatch a new message to a worker until it has processed and acknowledged the previous one.
Instead, it will dispatch it to the next worker that is not still busy.
"""
channel.basic_qos(
    prefetch_count=1,
    all_channels=False,
)

bc = channel.basic_consume(
    consumer_callback=callback,
    queue=QUEUE_NAME,
    no_ack=False,  # Tell the broker to expect an acknowledgement
)
print type(bc)  # <type 'str'>
print bc  # ctag1.da4a9beaf58b426aabdbefe390157bbf

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
print '----------------------------------------------------------------------------------------------------'
