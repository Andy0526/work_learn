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
    pg_master = 'dbname=sneaky user=sneaky password=77WN88wwc host=192.168.200.109'
    pg_shard = {
        1: 'dbname=sneaky user=sneaky password=77WN88wwc host=192.168.200.109',
        2: 'dbname=sneaky user=sneaky password=77WN88wwc host=192.168.100.110',
    }


def get_conns():
    conns = {}
    for shard_id, params in pg_shard.iteritems():
        conn = psycopg2.connect(params)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        conns[shard_id] = cur
    return conns


CONNS = get_conns()


def master_query(sql):
    cursor = CONNS[1]
    number = cursor.execute(sql)
    return cursor.fetchall()


def shard_query(sql):
    results = []
    for shard_id, cursor in CONNS.iteritems():
        number = cursor.execute(sql)
        res = cursor.fetchall()
        results.extend(res)
    return results
