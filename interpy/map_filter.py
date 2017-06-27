#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

def multiply(x):
    return (x * x)


def add(x):
    return (x + x)


def func_map():
    print '********func_map********'
    items = [i for i in range(10)]
    map_res = map(lambda x: x ** 2, items)
    print map_res

    funcs = [multiply, add]
    for i in range(5):
        value = map(lambda x: x(i), funcs)
        print(list(value))


def func_filter():
    print '********func_filter********'
    number_list = range(-5, 5)
    less_than_zero = filter(lambda x: x < 0, number_list)
    print(list(less_than_zero))


if __name__ == '__main__':
    func_map()
    func_filter()
