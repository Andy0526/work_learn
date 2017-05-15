#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan
import hashlib

# class MyClass(object):
#     def __init__(self, var1, var2, var3):
#         self.var1 = var1
#         self.var2 = var2
#         self.var3 = var3
#
#     def desc(self):
#         params = self.__dict__.copy()
#         del params['var1']
#         print params
#         print self.__dict__
#
#
# class1 = MyClass(1, 2, 3)
# class1.desc()
source = {'seller_email': 'rbtxzhfb@peiwo.cn', 'sign': '60e4e68f6b013459209d4a120b2c83ce',
          'subject': '498\\xe5\\x85\\x83\\xe7\\xa4\\xbc\\xe5\\x8c\\x85', 'is_total_fee_adjust': 'N',
          'gmt_create': '2017-04-07 18:14:56', 'out_trade_no': '331-208-1491560075559-684', 'sign_type': 'MD5',
          'price': '0.01', 'buyer_email': '532235905@qq.com', 'discount': '0.00', 'trade_status': 'TRADE_SUCCESS',
          'gmt_payment': '2017-04-07 18:15:11', 'trade_no': '2017040721001004950258145165',
          'seller_id': '2088421470785125', 'use_coupon': 'N', 'payment_type': '1', 'total_fee': '0.01',
          'notify_time': '2017-04-07 18:15:11', 'quantity': '1', 'notify_id': 'e9eae15285f145faee108c8a317c1d0nby',
          'notify_type': 'trade_status_sync', 'buyer_id': '2088112353381953'}

MD5_SELLER_PRIVATE_KEY = 'vvbr4zhcok9u5ofix4chssjjd4097ion'

source.pop('sign')
source.pop('sign_type')


def MD5_Sign(data):
    md5_obj = hashlib.md5()
    md5_obj.update(data)
    return md5_obj.hexdigest()


for key in sorted(source.keys()):
    print key

param_lst = ['{}={}'.format(k, source[k]) for k in sorted(source.keys())]

print '&'.join(param_lst) + MD5_SELLER_PRIVATE_KEY

print MD5_Sign('&'.join(param_lst) + MD5_SELLER_PRIVATE_KEY)
#
# source_1 = {'seller_email': 'rbtxzhfb@peiwo.cn', 'uid': '991', 'app': '1', 'sign': '80e20aa405b74965d352df97fbba5bfc',
#             'subject': '1\xe5\x85\x83\xe7\xa4\xbc\xe5\x8c\x85', 'password': 'e3ceb5881a0a1fdaad01296d7554868d',
#             'is_total_fee_adjust': 'N', 'gmt_create': '2017-03-13 17:23:10', 'version': '9999', 'sign_type': 'MD5',
#             'out_trade_no': '991-121-1489396959035-942', 'price': '0.01', 'buyer_email': '532235905@qq.com',
#             'discount': '0.00', 'trade_status': 'TRADE_SUCCESS', 'gmt_payment': '2017-03-13 17:23:18',
#             'trade_no': '2017031321001004950219883612', 'seller_id': '2088421470785125', 'use_coupon': 'N',
#             'payment_type': '1', 'total_fee': '0.01', 'notify_time': '2017-03-13 17:23:19',
#             'buyer_id': '2088112353381953', 'notify_id': '0df2f9117834e669bd9390abc5b0aaenby',
#             'notify_type': 'trade_status_sync', 'quantity': '1'}
#
# params_1 = {'seller_email': 'rbtxzhfb@peiwo.cn',
#             'subject': '1\xe5\x85\x83\xe7\xa4\xbc\xe5\x8c\x85',
#             'is_total_fee_adjust': 'N', 'gmt_create': '2017-03-13 17:23:10',
#             'out_trade_no': '991-121-1489396959035-942', 'price': '0.01', 'buyer_email': '532235905@qq.com',
#             'discount': '0.00', 'trade_status': 'TRADE_SUCCESS', 'gmt_payment': '2017-03-13 17:23:18',
#             'trade_no': '2017031321001004950219883612', 'seller_id': '2088421470785125', 'use_coupon': 'N',
#             'payment_type': '1', 'total_fee': '0.01', 'notify_time': '2017-03-13 17:23:19',
#             'buyer_id': '2088112353381953', 'notify_id': '0df2f9117834e669bd9390abc5b0aaenby',
#             'notify_type': 'trade_status_sync', 'quantity': '1'}
#
# print [key for key in params_1 if params_1[key] != source_1[key]]
# param1_lst = ['{}={}'.format(k, params_1[k]) for k in sorted(params_1.keys())]
# print '&'.join(param1_lst) + MD5_SELLER_PRIVATE_KEY
#
# print MD5_Sign('&'.join(param1_lst) + MD5_SELLER_PRIVATE_KEY)
#
# print set(params_1.keys()) - set(params.keys())
