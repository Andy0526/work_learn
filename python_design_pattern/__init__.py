#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan


class Signleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Signleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Signleton):
    a = 1


one = MyClass()
two = MyClass()

one.a = 2
print 'one.a={}'.format(one.a)
print 'two.a={}'.format(two.a)
print 'id(one):{}'.format(id(one))
print 'id(two):{}'.format(id(two))
print 'one==two: {}'.format(one == two)
print 'one is two: {}'.format(one is two)


class Brog(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Brog, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob


class MyClass2(Brog):
    a = 1


one = MyClass2()
two = MyClass2()

two.a = 3
print 'one.a={}'.format(one.a)
print 'two.a={}'.format(two.a)
print 'id(one):{}'.format(id(one))
print 'id(two):{}'.format(id(two))
print 'one==two: {}'.format(one == two)
print 'one is two: {}'.format(one is two)


class Singleton2(type):
    def __init__(cls, name, bases, dict):
        super(Singleton2, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__call__(*args, **kwargs)
        return cls._instance


class MyClass3(object):
    __metaclass__ = Singleton2


one = MyClass3()
two = MyClass3()

two.a = 3
print one.a
print id(one)
print id(two)
print one == two
print one is two


def singleton(cls):
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


@singleton
class MyClass4(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


one = MyClass4()
two = MyClass4()

two.a = 3
print one.a
print id(one), id(two)
print one == two
print one is two
one.x = 1
print one.x, two.x
