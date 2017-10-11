#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan


# def func():
#     print 'asas'
#     for i in range(10):
#         yield i
#

class MetaA(type):
    def __getattr__(cls, item):
        import traceback
        traceback.print_exc()
        print 'dadadas'
        return getattr(cls(), item, 'assadad')
    def who(cls):
        pass

class A(object):
    __metaclass__ = MetaA

print A.__dict__
a = A()
a.x = 1
print a.x
print A.x
