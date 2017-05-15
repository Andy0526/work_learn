#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

def func(num):
    global _num
    _num=10
    def _func():
        if num%2:
            global  _num
            print _num
            _num=2
            return _num
        return None

    res=_func()
    if res:
        _num=res
    print _num
    if not res:
        print 1111111111
        return
    print 22222222222
    return
func(10)
func(11)
