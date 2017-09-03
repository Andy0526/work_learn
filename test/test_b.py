#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

if __name__ == '__main__':
    import test_c

from contextlib import contextmanager


@contextmanager
def tag(name):
    print "<%s>" % name
    yield
    print "<%s>" % name


with tag('h1'):
    print 'foo'

print dir(tag)

def get():
    pass
print dir(get)