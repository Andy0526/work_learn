#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan
import pika
import time

connection = pika.BlockingConnection()
channel = connection.channel()
channel.queue_declare(queue='hello')
# channel.queue_declare(queue="hello",durable=True) #队列声明为持久化
print ' [*] Waiting for messages. To exit press CTRL+C'


def callback(ch, method, properities, body):
    print '[x] Received {}'.format(body)
    time.sleep(body.count('.'))
    print '[x] Done'
    ch.basic_ack(delivery_tag=method.delivery_tag)


# channel.basic_consume(callback, queue='hello', no_ack=True)
channel.basic_consume(callback, queue='hello') # 消息响应默认开启

channel.start_consuming()
