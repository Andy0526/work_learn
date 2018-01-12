# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

import psycopg2
import psycopg2.extras
from DBUtils.PooledDB import PooledDB



class DbManager():

    def __init__(self):
        connKwargs = {'host': '172.16.10.133', 'user': 'sneaky', 'password': '77WN88wwc', 'database': 'sneaky'}
        self._pool = PooledDB(psycopg2, mincached=0, maxcached=10, maxshared=10, maxusage=10000, **connKwargs)

    def getConn(self):
        return self._pool.connection()


_dbManager = DbManager()


def getConn():
    """ 获取数据库连接 """
    return _dbManager.getConn()


def execute(sql, param=None):
    """ 执行sql语句 """
    conn = getConn()
    cursor = conn.cursor()
    if param == None:
        rowcount = cursor.execute(sql)
    else:
        rowcount = cursor.execute(sql, param)
    cursor.close()
    conn.close()

    return rowcount


def query(sql):
    """ 获取所有信息 """
    conn = getConn()
    cursor = conn.cursor()
    rowcount = cursor.execute(sql)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res
