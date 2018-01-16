#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan
import logging
import sys

import time

from test_sync_relation_1.config import master_query, shard_query

sys.path.append('..')

formats = '[%(asctime)s] [%(filename)s L%(lineno)d] [%(levelname)s] %(message)s'
logging.basicConfig(level='DEBUG', format=formats, filename='log.txt')


def sync_block_data():
    logging.info('sync_block_data start')
    limit = 500
    offset = 0
    begin = time.time()
    query_sql = 'select uid,tuid,update_time from pw_block order by uid,tuid limit %s offset %s'
    while True:
        _begin = time.time()
        sql = query_sql % (limit, offset)
        res = master_query(sql)
        logging.info('sync_block_data_ limit:{},offset:{}, res:{}'.format(limit, offset, len(res)))
        if not res:
            break
        for each_data in res:
            uid = each_data['uid']
            tuid = each_data['tuid']
            block_query = 'select uid,tuid from pw_block where uid={} and tuid={}'.format(tuid, uid)
            block_res = master_query(block_query)
            contact_query = 'select uid,tuid from pw_contact where uid={} and tuid={}'.format(uid, tuid)
            contact_res = shard_query(contact_query)
            shard_sql = 'select shard_id,shard_key from pw_user_shard where shard_key in {}'.format(tuple([uid, tuid]))
            shard_res = master_query(shard_sql)
        i_len = len(res)
        offset += i_len
        logging.info(
            'sync_block_data_end. limit:{},offset:{}, res:{},avg_time:{}'.format(limit, offset, i_len,
                                                                                 (time.time() - _begin) / i_len))
    logging.info('sync_block_data end... avg_time:{}'.format((time.time() - begin) / offset))


def sync_contact_data():
    logging.info('sync_contact_data start...')
    limit = 500
    offset = 0
    query_sql = 'select uid,tuid,create_time from pw_contact where state!=1 order by uid,tuid limit %s offset %s'
    while True:
        sql = query_sql % (limit, offset)
        res = shard_query(sql)
        logging.info('sync_contact_data_ limit:{},offset:{}, res:{}'.format(limit, offset, len(res)))
        if not res:
            break
        for each_data in res:
            uid = each_data['uid']
            tuid = each_data['tuid']
            block_query = 'select uid,tuid from pw_block where uid={} and tuid={}'.format(tuid, uid)
            block_res = master_query(block_query)
            shard_sql = 'select shard_id,shard_key from pw_user_shard where shard_key in {}'.format(tuple([uid, tuid]))
            shard_res = master_query(shard_sql)
        offset += len(res)
    logging.info('sync_contact_data end...')


def sync_contact_req_data():
    logging.info('sync_contact_req_data start...')
    limit = 500
    offset = 0
    query_sql = 'select uid,tuid,create_time from pw_contact_request where state!=1 order by uid,tuid limit %s offset %s'
    while True:
        sql = query_sql % (limit, offset)
        res = shard_query(sql)
        logging.info('sync_contact_req_data limit:{},offset:{}, res:{}'.format(limit, offset, len(res)))
        if not res:
            break
        for each_data in res:
            uid = each_data['uid']
            tuid = each_data['tuid']
            block_query = 'select uid,tuid from pw_contact where state!=1 and uid={} and tuid={}'.format(tuid, uid)
            block_res = master_query(block_query)
            shard_sql = 'select shard_id,shard_key from pw_user_shard where shard_key in {}'.format(tuple([uid, tuid]))
            shard_res = master_query(shard_sql)
        offset += len(res)
    logging.info('sync_contact_req_data end...')


if __name__ == '__main__':
    sync_block_data()
    # sync_contact_data()
    # sync_contact_req_data()
