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
    print additon_func.__name__


def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print log_string
            with open(logfile, 'a') as f:
                f.write(log_string + '\n')
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator


@logit()
def myfunc1():
    pass


@logit(logfile='func2.log')
def myfunc2():
    pass


def logit_test():
    myfunc1()
    myfunc2()


import traceback


class logit_cls(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + ' was called...'
            print log_string
            traceback.print_stack()
            with open(self.logfile, 'a') as f:
                f.write(log_string + '\n')
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        pass


@logit_cls()
def my_func1():
    pass

if __name__ == '__main__':
    # my_func_1()
    # additon_func_test()
    # logit_test()
    my_func1()
