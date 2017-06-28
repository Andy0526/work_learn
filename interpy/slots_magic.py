#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

class MyClass1(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


class MyClass2(object):
    __slots__ = ['name', 'identifier']

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
