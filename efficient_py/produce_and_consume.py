#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

import random


def get_data():
    return random.sample(range(10), 3)


def consume():
    running_sum = 0
    data_items_seen = 0
    while True:
        print 'Waiting to consume'
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
        print "Consumed, the running average is {}".format(running_sum / float(data_items_seen))


def produce(consumer):
    while True:
        data = get_data()
        print 'Produced {}.'.format(data)
        consumer.send(data)
        yield


if __name__ == '__main__':
    consumer = consume()
    consumer.next()
    # consumer.send(None)
    producer = produce(consumer)
    for _ in range(10):
        print 'Producing...'
        next(producer)
