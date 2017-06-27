#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

from functools import reduce


def my_reduce():
    product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
    print product

if __name__ == '__main__':
    my_reduce()
