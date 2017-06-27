#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

"""Serve

Usage:
  serve.py -t <type>

Options:
  -h --help     Show this screen.
  -v --version     Show version.
"""
from docopt import docopt
if __name__ == '__main__':
    arguments = docopt(__doc__, version='Serve 1.0')
    print(arguments)


# Description: 各服务启动脚本
#
# Usage:
#     python %s [options]
#
# OPTIONS:
#    -h    查看帮助文档
#    -t    类型
#    -e    环境(对于与config下的py文件, 必填)
#    -p    端口(option)
#    -q    队列名(option)
#    -a    admin服务,是否启动admin服务
#    -l    等级(option, timer专用)
#    -c    分片总数(option, timer专用)
#    -i    间隔(option, matcher专用)
#    -m    男性匹配池名称(option, matcher专用)
#    -f    女性匹配池名称(option, matcher专用)
#
# 参数t(服务类型)种类:
# -- hub: tcp接入层服务
#    参数: -q 订阅消息队列地址
#    参数: -p hub监听的端口
# -- api: web服务
#    参数: -p api服务监听的端口
#         -a 是否启动admin api
# -- worker: worker服务, 主要处理短信等其他业务
#    参数: -q 订阅消息队列地址
# -- call_worker: call_worker服务, 主要处理电话业务
#    参数: -q 订阅消息队列地址
# -- signin_worker: signin_worker服务, 主要长连接鉴权登录业务
#    参数: -q 订阅消息队列地址
# -- timer: 定时器模块,主要负责计费
#    参数: -c 分片总数
#         -l 当前分片层(0<=l<c)
# -- matcher: 匿名聊匹配模块
#    参数: -i 匹配间隔
#         -m 男性匹配池
#         -f 女性匹配池
# -- recommender: 用户推荐模块
#    参数: -p 服务监听的端口
# -- welcome: 用户受欢迎程度推荐模块
#    参数: -p 服务监听的端口
# -- userlist: 用户信息缓存模块
#    参数: -p 服务监听的端口
# -- feedpub: 信息流缓存模块
#    参数: -p 服务监听的端口
# -- event: 事件处理模块
# -- snapshot: 群快照模块
# -- fetch_gchat_messages: 群消息统计模块
# -- candidate_loader: 秒配用户加载模块
# -- statistics: 日报统计模块
#
# 例子:
# 1) 启动api
# python serve.py -t api -p 8920 (不启动admin)
# python serve.py -t api -p 8920 -a (启动admin)
#
# 2) 启动hub(根据type命名队列,同一queue上不要创建相同的type)
# python serve.py -t hub1 -p 8900 -q rabbitmq.cluster1.master
# python serve.py -t hub2 -p 9900 -q rabbitmq.cluster1.master
# python serve.py -t hub3 -p 8900 -q rabbitmq.cluster1.master
# python serve.py -t hub4 -p 9900 -q rabbitmq.cluster1.master
#
# python serve.py -t hub1 -p 8900 -q rabbitmq.cluster2.master
# python serve.py -t hub2 -p 9900 -q rabbitmq.cluster2.master
# python serve.py -t hub3 -p 8900 -q rabbitmq.cluster2.master
# python serve.py -t hub4 -p 9900 -q rabbitmq.cluster2.master
#
# python serve.py -t hub1 -p 8900 -q rabbitmq.cluster3.master
# python serve.py -t hub2 -p 9900 -q rabbitmq.cluster3.master
# python serve.py -t hub3 -p 8900 -q rabbitmq.cluster3.master
# python serve.py -t hub4 -p 9900 -q rabbitmq.cluster3.master
#
# 3) 启动worker
# python serve.py -t worker -q rabbitmq.cluster1.master
#
# 4) 启动call_worker
# python serve.py -t call_worker -q rabbitmq.cluster1.master
#
# 5) 启动signin_worker
# python serve.py -t signin_worker -q rabbitmq.cluster1.master
#
# 6) 启动matcher
# python serve.py -t matcher -i 1.5 -m wild_male_pool_low -f wild_female_pool_low
#
# 7) 启动timer
# python serve.py -t timer -c 4 -l 0
# python serve.py -t timer -c 4 -l 1
# python serve.py -t timer -c 4 -l 2
# python serve.py -t timer -c 4 -l 3
#
# 8) 启动event
# python serve.py -t event
#
# 9) 启动recommender
# python serve.py -t recommender 10001
#
# 10) 启动welcome
# python serve.py -t welcome -p 20001
#
# 11) statistics
# python serve.py -t statistics
#
# 12) live
# python serve.py -t live -c 2 -l 0
# python serve.py -t live -c 2 -l 1
#
# 13) finance
# python serve.py -t finance
#
# 14) 启动userlist
# python serve.py -t userlist -p 20002
#
# 14) 启动feedpub
# python serve.py -t feedpub -p 20003