#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

# class M1(type):
#     def __new__(meta, name, bases, atts):
#         print 'M1 called for ' + name
#         return super(M1, meta).__new__(meta, name, bases, atts)
#
#
# class C1(object):
#     __metaclass__ = M1
#
#
# class SubC1(C1):
#     pass
#
#
# class M2(type):
#     def __new__(meta, name, bases, atts):
#         print 'M2 called for ' + name
#         return super(M2, meta).__new__(meta, name, bases, atts)
#
#
# class C2(object):
#     __metaclass__ = M2
#
#
# # metaclass conflict
# # class SubC(C1, C2):
# #     pass
#
# class M3(M2, M1):
#     def __new__(meta, name, bases, atts):
#         print 'M3 called for ' + name
#         return super(M3, meta).__new__(meta, name, bases, atts)
#
#
# class C3(C1, C2):
#     __metaclass__ = M3
class Manager(object):
    def __init__(self, managed_obj):
        self.managed_obj = managed_obj

class MyObj(object):
    def __new__(cls, *args, **kwargs):
        ob = super(MyObj, cls).__new__(cls, *args, **kwargs)
        if not hasattr(cls,'manager'):
            cls.manager = Manager(cls)
        return ob

m1 = MyObj()
m2 = MyObj()
print id(m1.manager)
print id(m2.manager)
print m1.manager