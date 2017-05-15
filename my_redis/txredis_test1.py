#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

import txredisapi as redis

from twisted.internet import defer, reactor


# @defer.inlineCallbacks
# def main():
#     rc = yield redis.Connection()
#     print rc
#
#     yield rc.set('foo', 'bar')
#
#     v = yield rc.get('foo')
#     print "foo:{}".format(v)
#
#     import traceback
#     traceback.print_stack()
#     yield rc.disconnect()
#
#
# if __name__ == '__main__':
#     main().addCallback(lambda ign: reactor.stop())
#     reactor.run()

import redis
r=redis.Redis()


def sleep(n):
    d = defer.Deferred()
    reactor.callLater(5, lambda *ign: d.callback(None))
    return d


@defer.inlineCallbacks
def main():
    rc = yield redis.Connection()
    print rc

    res = yield rc.setnx('foo2', 'bar')
    print res

    print 'sleep for 5s,kill redis now!'

    # yield sleep(5)
    # print "sleep done"
    try:
        v = yield rc.get('foo1')
        print 'foo1', v
        yield rc.disconnect()
    except redis.ConnectionError, e:
        print str(e)


if __name__ == '__main__':
    main().addCallback(lambda ign: reactor.stop())
    reactor.run()
