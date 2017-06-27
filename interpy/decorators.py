#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

from functools import wraps

import request


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)

    return decorated


@decorator_name
def func():
    return ("Function is running")


can_run = True


def my_func_1():
    print(func())
    global can_run
    can_run = False
    print(func())


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print "{} was called".format(func.__name__)
        return func(*args, **kwargs)

    return with_logging


@logit
def additon_func(x):
    return x + x


def additon_func_test():
    additon_func(4)


if __name__ == '__main__':
    my_func_1()
    additon_func_test()
