#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan
import logging
from multiprocessing.pool import ThreadPool

import time

from sync_user_relation import config
from sync_user_relation_old.config import get_in_tuple, split_list, conns

thread_pool = ThreadPool(processes=4)

formats = '[%(asctime)s] [%(filename)s L%(lineno)d] [%(levelname)s] [' + '] %(message)s'
logging.basicConfig(level='DEBUG', format=formats)


def get_block_data(page_size):
    logging.info('get_block_data  page_size:{} start...'.format(page_size))
    begin = time.time()
    query_sql = 'select uid,tuid,update_time from pw_block ' \
                'order by uid,tuid limit 5000 offset {}'.format(page_size * 5000)
    conn = config.MASTER.getconn()
    cursor = conn.cursor()
    cursor.execute(query_sql)
    results = []
    block_uids = set()
    for res in cursor.fetchall():
        results.append(res)
        block_uids.add((res[0], res[1]))
    logging.info('get_block_data  page_size:{} end. runtime:{}'.format(page_size, time.time() - begin))
    return results, block_uids


def get_all_block_data():
    begin = time.time()
    logging.info('get_all_block_data start...')
    block_datas = []
    page_lst = range(3)
    results = thread_pool.map(get_block_data, page_lst)
    logging.info('get_all_block_data end. runtime:{}'.format(time.time() - begin))
    block_uids_lst = []
    for res, block_uids in results:
        block_datas.extend(res)
        block_uids_lst.extend(list(block_uids))
    return block_datas, block_uids_lst


def get_contact_data(uid_lst):
    begin = time.time()
    logging.info('get_all_block_data start...')
    pieces = split_list(uid_lst)
    for piece in pieces:
        _begin = time.time()
        logging.info('piece_get_contact_data uid_piece:{} {} start...'.format(len(piece), piece[:10]))
        uids_lst = get_in_tuple(piece)
        query_sql = 'select uid,tuid from pw_contact ' \
                    'where uid in {} or tuid in {}'.format(uids_lst, uids_lst)
        cursor = conns[1]
        cursor.execute(query_sql)
        frd_lst = []
        for res in cursor.fetchall():
            frd_lst.append((res['uid'], res['tuid']))
        logging.info('piece_get_contact_data uid_piece:{} {} end. runtime:{}'.format(len(piece), piece[:10],
                                                                                     time.time() - _begin))
    logging.info('get_all_block_data end. runtime:{}'.format(time.time() - begin))


def mul_get_block_data(uid_lst):
    begin = time.time()
    logging.info('mul_thread_get_block_data start...')
    pieces = split_list(uid_lst)
    for piece in pieces:
        _begin = time.time()
        logging.info('piece_get_block_data uid_piece:{} {} start...'.format(len(piece), piece[:10]))
        uids_lst = get_in_tuple(piece)
        query_sql = 'select uid,tuid from pw_block ' \
                    'where uid in {} or tuid in {}'.format(uids_lst, uids_lst)
        cursor = conns[1]
        cursor.execute(query_sql)
        block_lst = []
        for res in cursor.fetchall():
            block_lst.append((res['uid'], res['tuid']))
        logging.info('thread_get_block_data uid_piece:{} {} end. runtime:{}'.format(len(piece), piece[:10],
                                                                                    time.time() - _begin))

    logging.info('mul_thread_get_block_data end. runtime:{}'.format(time.time() - begin))


def get_shard_data(uid_lst):
    begin = time.time()
    logging.info('get_shard_data start...')
    pieces = split_list(uid_lst)
    for piece in pieces:
        _begin = time.time()
        logging.info('piece_get_block_data uid_piece:{} {} start...'.format(len(piece), piece[:10]))
        uids_lst = get_in_tuple(piece)
        query_sql = 'select shard_id,shard_key from pw_user_shard ' \
                    'where shard_key in {}'.format(uids_lst)
        cursor = conns[1]
        cursor.execute(query_sql)
        shard_data = {res['shard_id']: res['shard_key'] for res in cursor.fetchall()}
        logging.info('piece_get_block_data uid_piece:{} {} end. runtime:{}'.format(len(piece), piece[:10],
                                                                                   time.time() - _begin))

    logging.info('get_shard_data end. runtime:{}'.format(time.time() - begin))


def sync_block():
    block_datas, block_uids_lst = get_all_block_data()
    uid_lst = set()
    for uids_pair in block_uids_lst:
        uid_lst.update(uids_pair)
    uid_lst = list(uid_lst)
    get_contact_data(uid_lst)
    get_shard_data(uid_lst)


def sync_contact_data():
    offset = 0
    while True:
        query_sql = 'select uid,tuid,create_time from pw_contact where state!=1 ' \
                    'order by uid,tuid limit 5000 offset {}'.format(offset)
        cursor = conns[1]
        cursor.execute(query_sql)
        frd_lst = []
        uids_set = set()
        for res in cursor.fetchall():
            frd_pair = res['uid'], res['tuid']
            frd_lst.append(frd_pair)
            uids_set.update(frd_pair)
        if not frd_lst:
            break
        uid_lst = list(uids_set)
        mul_get_block_data(uid_lst)
        get_shard_data(uid_lst)
        offset += 5000


def sync_contact_req_data():
    offset = 0
    while True:
        query_sql = 'select uid,tuid,update_time from pw_contact_request where state!=1 ' \
                    'order by uid,tuid limit 5000 offset {}'.format(offset)
        cursor = conns[1]
        cursor.execute(query_sql)
        contact_req_lst = []
        uids_set = set()
        for res in cursor.fetchall():
            req_pair = res['uid'], res['tuid']
            contact_req_lst.append(req_pair)
            uids_set.update(req_pair)
        if not contact_req_lst:
            break
        uid_lst = list(uids_set)
        get_contact_data(uid_lst)
        get_shard_data(uid_lst)
        offset += 5000


if __name__ == '__main__':
    sync_block()
    sync_contact_data()
    sync_contact_req_data()
