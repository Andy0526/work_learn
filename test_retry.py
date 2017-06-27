#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

from retrying import retry, RetryError

from exceptions import StandardError, StopIteration

import random

# class MyException(Exception):
#     def __init__(self, desc):
#         self.desc = desc
#
#     def __str__(self):
#         return str(self.desc)
#
#
# def retry_if_standerr(exception):
#     # import traceback
#     # traceback.print_exc()
#     print exception
#     # print isinstance(exception, IndexError)
#     return isinstance(exception, MyException)
#
#
# @retry(stop_max_attempt_number=5, retry_on_exception=retry_if_standerr)
# def test_retry():
#     raise MyException('this is my exception')
#     # try:
#     #     raise random.choice([StandardError, StopIteration])
#     # except StandardError:
#     #     raise StandardError
#     # except:
#     #     print 'err:', StopIteration
#
#
# test_retry()


# def fuunc_1():
#     global var
#     var =0
#
#     def _func1():
#         global var
#         var=2
#     _func1()
#     print var
#
# if __name__ == '__main__':
#     fuunc_1()

from retrying import retry


# class A(object):
#     bar = 1
#     def foo(self):
#         print 'foo'
#
#     @staticmethod
#     def static_foo():
#         print 'static_foo'
#         print A.bar
#
#     @classmethod
#     def class_foo(cls):
#         print 'class_foo'
#         print cls.bar
#         cls().foo()
#     @staticmethod
#     def retry_on_result(self,var):
#         return isinstance(var)
#     @retry(stop_max_attempt_number=3,retry_on_result=A.retry_on_result)
#     def test(self):
#         return self
#
# a=A()
# a.test()



# def retry_on_result(res):
#     return res != 8
#
#
# def retry_on_excep(exception):
#     print "retry_on_excep"
#     if isinstance(exception, RetryError):
#         return True
#     return False
#
#
# @retry(retry_on_exception=retry_on_excep)
# def func(n):
#     @retry(stop_max_attempt_number=5, retry_on_result=retry_on_result)
#     def _func():
#         return random.randint(0, n)
#
#     return _func()


# _retry=retry
#
# def myretry():
#     try:
#         _retry()
#     except:
#         pass


class MyException(Exception):
    pass


idx = 0


def retry_on_excep(exception):
    global idx
    idx += 1
    print idx
    return isinstance(exception, MyException)


@retry(stop_max_attempt_number=3, retry_on_exception=retry_on_excep)
def func(n):
    if n % 2:
        raise MyException()
    else:
        print n


func(2)
func(1)
