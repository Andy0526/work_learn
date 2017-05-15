#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

message = ' '.join(sys.argv[1:]) or "Hello rabbitmq"

channel.queue_declare(queue='task_queue', durable=True)

channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))

print "[x] Sent '{}'".format(message)

connection.close()
