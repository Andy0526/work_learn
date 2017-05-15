#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

message = ' '.join(sys.argv[1:]) or "Hello rabbitmq"

# channel.queue_declare(queue="hello")

channel.queue_declare(queue="hello", durable=True)  # 队列声明为持久化

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2,  # make message persisitent
                    ))
print "[x] Sent '{}'".format(message)

connection.close()
