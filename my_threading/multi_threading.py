#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan
from multiprocessing.dummy import Pool as ThreadPool

import psycopg2
import psycopg2.extras

TEST = True
if TEST:
    mongo_uri = '172.16.10.130:22000'
    pg_master = 'dbname=sneaky user=sneaky password=77WN88wwc host=172.16.10.133'
    pg_shard = [
        'dbname=sneaky user=sneaky password=77WN88wwc host=172.16.10.133',
        'dbname=sneaky user=sneaky password=77WN88wwc host=172.16.10.162',
        'dbname=sneaky user=sneaky password=77WN88wwc host=172.16.10.162']
else:
    mongo_uri = '192.168.100.2:22000'
    pg_master = 'dbname=sneaky user=sneaky password=77WN88wwc host=192.168.100.1'
    pg_shard = [
        'dbname=sneaky user=sneaky password=77WN88wwc host=192.168.100.1',
        'dbname=sneaky user=sneaky password=77WN88wwc host=192.168.100.21']


def get_conn(url):
    conn = psycopg2.connect(url)
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    return cur


MASTER = get_conn(pg_master)


def get_block_data(page_size):
    query_sql = 'select uid,tuid,update_time from pw_block order by uid,tuid limit 5000 offset {}'.format(
        page_size * 5000)
    cursor = MASTER
    cursor.execute(query_sql)
    results = []
    for res in cursor.fetchall():
        print res
        results.append(res)
    return results


def get_all_block_data():
    page_lst = range(10)
    pool = ThreadPool(processes=2)
    results = pool.map(get_block_data, page_lst)

    print results
    pool.close()
    pool.join()


if __name__ == '__main__':
    get_all_block_data()
