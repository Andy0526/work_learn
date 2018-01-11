#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan
from multiprocessing.pool import ThreadPool

from psycopg2.pool import ThreadedConnectionPool

pool = ThreadedConnectionPool(minconn=4,
                              maxconn=100,
                              database='sneaky',
                              user='sneaky',
                              password='77WN88wwc',
                              host='172.16.10.133',
                              )


def get_block_data(page_size):
    query_sql = 'select uid,tuid,update_time from pw_block order by uid,tuid limit 100 offset {}'.format(
        page_size * 100)
    conn = pool.getconn()
    cursor = conn.cursor()
    results = []
    cursor.execute(query_sql)
    for res in cursor.fetchall():
        results.append(res)
    return results


def get_all_block_data():
    page_lst = range(4)
    pool = ThreadPool(processes=4)
    results = pool.map(get_block_data, page_lst)
    block_data = []
    for res in results:
        block_data.extend(res)
    print len(block_data), block_data
    pool.close()
    pool.join()


if __name__ == '__main__':
    get_all_block_data()
