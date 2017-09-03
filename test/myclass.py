#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

class A():
    _c = 'test'

    def __init__(self):
        self.x = None

    @property
    def a(self):
        print 'using property to access attribute'
        if not self.x:
            print 'return value'
            return 'a'
        else:
            print "error occured"
            raise AttributeError

    @a.setter
    def a(self, value):
        print 'using a.setter to set attribute a'
        self.x = value

    def __getattr__(self, name):
        print 'using __getattr__ to access attribute'
        print 'attribute name: ', name
        return 'b'

    def __getattribute__(self, item):
        print 'using __getattribute__ to access attribute'
        return object.__getattribute__(self, item)


a1 = A()
print a1.a
print '---------------------------'
a1.a = 1
print a1.a
print '---------------------------'
print A._c
print a1._c
