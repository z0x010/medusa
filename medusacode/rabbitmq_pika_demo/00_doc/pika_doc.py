#!/usr/bin/env python
# coding:utf-8

"""
pika
http://pika.readthedocs.org/en/0.10.0/
"""

"""
class pika.adapters.blocking_connection.BlockingConnection(parameters=None, _impl_class=None)
    The BlockingConnection creates a layer on top of Pika’s asynchronous core
    providing methods that will block until their expected response has returned.
    Due to the asynchronous nature of the Basic.Deliver and Basic.Return calls from RabbitMQ to your application,
    you can still implement continuation-passing style asynchronous methods
    if you’d like to receive messages from RabbitMQ using basic_consume
    or if you want to be notified of a delivery failure when using basic_publish.

BlockingConnection.channel(channel_number=None)[source]
    Create a new channel with the next available channel number or pass in a channel number to use.
    Must be non-zero if you would like to specify but it is recommended that you let Pika manage the channel numbers.
    Return type:
        pika.synchronous_connection.BlockingChannel
"""

"""
class pika.channel.Channel(connection, channel_number, on_open_callback=None)
    A Channel is the primary communication method for interacting with RabbitMQ.
    It is recommended that you do not directly invoke the creation of a channel object in your application code
    but rather construct the a channel by calling the active connection’s channel() method.

Channel.queue_declare(callback, queue='', passive=False, durable=False, exclusive=False, auto_delete=False, nowait=False, arguments=None)
    Declare queue, create if needed.
    This method creates or checks a queue.
    When creating a new queue the client can specify various properties that
    control the durability of the queue and its contents, and the level of sharing for the queue.
    Leave the queue name empty for a auto-named queue in RabbitMQ.
    Parameters:
        callback (method) – The method to call on Queue.DeclareOk
        queue (str or unicode) – The queue name
        passive (bool) – Only check to see if the queue exists
        durable (bool) – Survive reboots of the broker
        exclusive (bool) – Only allow access by the current connection
        auto_delete (bool) – Delete after consumer cancels or disconnects
        nowait (bool) – Do not wait for a Queue.DeclareOk
        arguments (dict) – Custom key/value arguments for the queue
"""

"""
Channel.basic_publish(exchange, routing_key, body, properties=None, mandatory=False, immediate=False)
    Publish to the channel with the given exchange, routing key and body.
    Parameters:
        exchange (str or unicode) – The exchange to publish to
        routing_key (str or unicode) – The routing key to bind on
        body (str or unicode) – The message body
        properties (pika.spec.BasicProperties) – Basic.properties
        mandatory (bool) – The mandatory flag
        immediate (bool) – The immediate flag

Channel.basic_consume(consumer_callback, queue='', no_ack=False, exclusive=False, consumer_tag=None, arguments=None)
    Sends the AMQP command Basic.Consume to the broker and binds messages for the consumer_tag to the consumer_callback.
    If you do not pass in a consumer_tag, one will be automatically generated for you.
    Returns the consumer_tag.
    Parameters:
        consumer_callback (method) – The method to callback when consuming with the signature
            consumer_callback(channel, method, properties, body)
                channel: BlockingChannel
                method: spec.Basic.Deliver
                properties: spec.BasicProperties
                body: str or unicode
        queue (str or unicode) – The queue to consume from
        no_ack (bool) – Tell the broker to not expect a response
        exclusive (bool) – Don’t allow other consumers on the queue
        consumer_tag (str or unicode) – Specify your own consumer tag
        arguments (dict) – Custom key/value pair arguments for the consume
"""

"""
Channel.basic_qos(callback=None, prefetch_size=0, prefetch_count=0, all_channels=False)
    Specify quality of service.
    This method requests a specific quality of service.
    The QoS can be specified for the current channel or for all channels on the connection.
    The client can request that messages be sent in advance so that when the client finishes processing a message,
    the following message is already held locally, rather than needing to be sent down the channel.
    Prefetching gives a performance improvement.
    Parameters:
        callback (method) – The method to callback for Basic.QosOk response
        prefetch_size (int) – This field specifies the prefetch window size.
            The server will send a message in advance if it is equal to or smaller in size than
            the available prefetch size (and also falls into other prefetch limits).
            May be set to zero, meaning “no specific limit”, although other prefetch limits may still apply.
            The prefetch-size is ignored if the no-ack option is set.
        prefetch_count (int) – Specifies a prefetch window in terms of whole messages.
            This field may be used in combination with the prefetch-size field;
            a message will only be sent in advance if both prefetch windows (and those at the channel and connection level) allow it.
            The prefetch-count is ignored if the no-ack option is set.
        all_channels (bool) – Should the QoS apply to all channels
"""


