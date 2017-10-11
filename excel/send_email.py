#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan
from util.mail_util import send_email

address = ['liujintong@peiwo.cn','532235905@qq.com','jiangxiaoqiang@peiwo.cn' ]

send_email(address, '测试发送', '测试发送', files=['../【陪我APP】测试1720170922直播信息统计报表.xls',])
# import os
# print os.getcwd()