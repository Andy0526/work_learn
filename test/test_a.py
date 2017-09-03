#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print 'Retrieving', self.name
        return self.val

    def __set__(self, obj, val):
        print 'Updating', self.name
        self.val = val


class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5

    def __init__(self):
        self.z = 1


# m = MyClass()
# m.x
#
# m.x = 20
# print m.__dict__
# print MyClass.__dict__

a = MyClass()
a.y = 2
b = MyClass()
print type(a).__dict__['y']
print a.y, a.__dict__
print b.y
