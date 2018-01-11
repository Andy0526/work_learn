#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

import psycopg2
import psycopg2.extras
TEST = True
if TEST:
    mongo_uri = '172.16.10.130:22000'
    pg_master = 'dbname=sneaky user=sneaky password=77WN88wwc host=172.16.10.133'
    pg_shard = {
        1: 'dbname=sneaky user=sneaky password=77WN88wwc host=172.16.10.133',
        2: 'dbname=sneaky user=sneaky password=77WN88wwc host=172.16.10.162',
        3: 'dbname=sneaky user=sneaky password=77WN88wwc host=172.16.10.168',
    }
else:
    pg_master = 'dbname=sneaky user=sneaky password=77WN88wwc host=192.168.200.12'
    pg_shard = {
        1: 'dbname=sneaky user=sneaky password=77WN88wwc host=192.168.200.12',
        2: 'dbname=sneaky user=sneaky password=77WN88wwc host=192.168.100.110',
    }


def get_conns():
    conns = {}
    for shard_id, params in pg_shard.iteritems():
        conn = psycopg2.connect(params)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        conns[shard_id] = cur
    return conns


conns = get_conns()


class USER_RELATION_INFO(object):
    NORMAL = 0
    LIKED = 1
    LIKE = 2
    FRIEND = 3
    STRANGER_BLOCKED = 4
    FRD_BLOCKED = 7
    STRANGER_BLOCK = 8
    FRD_BLOCK = 11
    STRANGER_INTER_BLOCK = 12
    FRD_INTER_BLOCK = 15


def split_list(data, page_size=10000):
    count_all = len(data)
    if count_all % page_size > 0:
        page_count = count_all / page_size + 1
    else:
        page_count = count_all / page_size
    pieces = [data[each * page_size: (each + 1) * page_size] for each in range(page_count)]
    return pieces


def get_in_tuple(args):
    args = list(args)
    if len(args) == 1:
        args.append(args[0])
    return tuple(args)


from psycopg2.pool import ThreadedConnectionPool

if TEST:
    SHARD_1_POOL = ThreadedConnectionPool(minconn=4,
                                          maxconn=100,
                                          database='sneaky',
                                          user='sneaky',
                                          password='77WN88wwc',
                                          host='172.16.10.133',
                                          )
    SHARD_2_POOL = ThreadedConnectionPool(minconn=4,
                                          maxconn=100,
                                          database='sneaky',
                                          user='sneaky',
                                          password='77WN88wwc',
                                          host='172.16.10.162',
                                          )
    SHARD_3_POOL = ThreadedConnectionPool(minconn=4,
                                          maxconn=100,
                                          database='sneaky',
                                          user='sneaky',
                                          password='77WN88wwc',
                                          host='172.16.10.168',
                                          )

    DB_POOLS = {
        1: SHARD_1_POOL,
        2: SHARD_2_POOL,
        3: SHARD_3_POOL,
    }
    MASTER = SHARD_1_POOL
