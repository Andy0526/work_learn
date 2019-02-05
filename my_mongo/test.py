#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

import sys
import time

from twisted.internet import reactor
from twisted.python import log

import txmongo

MONGDB_SERVERS = {
    'host': '172.16.10.130',
    'port': 22000,
    'pool_size': 6
}


def updateData(ignored, conn):
    print "updating data..."
    collection = conn.sneaky.pw_feed_pub
    d = collection.update(
        {"uid": 442}, {"$set": {"state": 1}}, safe=True)
    d.addErrback(log.err)
    return d


def insertData(conn):
    print "inserting data..."
    collection = conn.sneaky.pw_feed_pub
    d = collection.find_one({"uid": 442})
    d.addErrback(log.err)
    d.addCallback(updateData, conn)
    return d


def finish(ignore):
    print "finishing up..."
    reactor.stop()


def example():
    d = txmongo.MongoConnection(**MONGDB_SERVERS)
    d.addCallback(insertData)
    d.addCallback(finish)
    return d


if __name__ == '__main__':
    log.startLogging(sys.stdout)
    example()
    reactor.run()
