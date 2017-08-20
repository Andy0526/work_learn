#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan


def return_test(a):
    try:
        if a <= 0:
            raise ValueError('data can not be negative')
        else:
            a = 2
            return a
    except ValueError as e:
        print e
    finally:
        print ("The end!")
        a = -1
        return a


print return_test(0)
print return_test(2)
