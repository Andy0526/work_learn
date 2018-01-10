#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan
from multiprocessing.pool import ThreadPool

import psycopg2
import psycopg2.extras

from sync_user_relation import config
from sync_user_relation.config import pg_shard


def get_conns():
    conns = {}
    for shard_id, params in pg_shard.iteritems():
        conn = psycopg2.connect(params)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        conns[shard_id] = cur
    return conns


thread_pool = ThreadPool(processes=20)


def get_block_data(page_size):
    query_sql = 'select uid,tuid,update_time from pw_block order by uid,tuid limit 5000 offset {}'.format(
        page_size * 5000)
    conn = config.MASTER.getconn()
    cursor = conn.cursor()
    cursor.execute(query_sql)
    results = []
    for res in cursor.fetchall():
        results.append(res)
    conn.putconn()
    return results


def get_all_block_data():
    block_datas = []
    page_lst = range(3)
    results = thread_pool.map(get_block_data, page_lst)
    for res in results:
        block_datas.extend(res)
    print len(block_datas)
    return block_datas


def get_contact_data(page_size):
    contact_datas = []
    query_sql = 'select uid,tuid,create_time from pw_contact where state!=1 ' \
                'order by uid,tuid limit 5000 offset {}'.format(page_size * 5000)
    part_data = []
    conn = config.MASTER.getconn()
    cursor = conn.cursor()
    cursor.execute(query_sql)
    results = []
    for res in cursor.fetchall():
        results.append(res)
    conn.putconn()

#
#
# def get_all_contact_req_data():
#     offset = 0
#     limit = 10000
#
#     contact_req_datas = []
#     while True:
#         query_sql = 'select uid,tuid,state,update_time as create_time from pw_contact_request ' \
#                     'where state!=1 order by uid,tuid limit {limit} offset({offset})'.format(
#             limit=limit, offset=offset)
#         part_data = []
#         for cur in PG_CONNS.itervalues():
#             cur.execute(query_sql)
#             for res in cur.fetchall():
#                 part_data.append(res)
#         if not part_data:
#             break
#         contact_req_datas.extend(part_data)
#         offset += limit
#         print 'get_all_contact_req_data', offset
#     return contact_req_datas
#
#
# def get_all_shard_data():
#     offset = 0
#     limit = 10000
#
#     shard_datas = {}
#     while True:
#         query_sql = 'select shard_key,shard_id from pw_user_shard  ' \
#                     'order by shard_key limit {limit} offset({offset})'.format(
#             limit=limit, offset=offset)
#         part_data = []
#         cur = PG_CONNS[1]
#         cur.execute(query_sql)
#         for res in cur.fetchall():
#             part_data.append(res)
#         if not part_data:
#             break
#         shard_datas.update({res['shard_key']: res['shard_id'] for res in part_data})
#         offset += limit
#         print 'get_all_shard_data', offset
#     return shard_datas
#
#
# def sync_user_relations():
#     # block_datas = get_all_block_data()
#     # contact_datas = get_all_contact_data()
#     # contact_req_datas = get_all_contact_req_data()
#     shard_datas = get_all_shard_data()
#     print 'end'
#     # existed_relations = set()
#     # sync_block_relation(block_datas, contact_datas, shard_datas, existed_relations)
#
#
# def sync_block_relation(block_res, contact_datas, shard_data, existed_relations):
#     logging.info('sync_user_relation__ sync_block start...')
#     begin = time.time()
#     block_uids = set()
#     block_data = {}
#     for res in block_res:
#         block_data[(res['uid'], res['tuid'])] = res
#         block_uids.add(res['uid'])
#         block_uids.add(res['tuid'])
#     block_uid_pairs = block_data.keys()
#     block_uid_pairs2 = [(tuid, uid) for uid, tuid in block_data.keys()]
#     columns = ['uid', 'tuid', 'relation_type', 'update_time', ]
#     inter_block_uids = set(block_uid_pairs) & set(block_uid_pairs2)
#     block_uids_set = set()
#     inter_block_lst = []
#     block_lst = []
#     for block_key, block_value in block_data.iteritems():
#         if block_key in inter_block_uids:
#             inter_block_lst.append(block_value)
#         else:
#             block_uids_set.add(block_key)
#             block_lst.append(block_value)
#     frd_lst = [(res['uid'], res['tuid']) for res in contact_datas]
#     sync_frd_inter_block(inter_block_lst, columns, frd_lst, shard_data, existed_relations)
#     sync_frd_block(block_lst, columns, frd_lst, shard_data, existed_relations)
#     logging.info('sync_user_relation__ sync_block end, runtime:{}'.format(time.time() - begin))
#
#
# def sync_frd_inter_block(inter_block_lst, columns, frd_lst, shard_data, existed_relations):
#     pieces = split_list(inter_block_lst)
#     for piece in pieces:
#         frd_bind_placeholds = {}
#         frd_values = {}
#         stranger_bind_placeholds = {}
#         stranger_values = {}
#         insert_uids = []
#         for inter_block in piece:
#             uid = inter_block['uid']
#             tuid = inter_block['tuid']
#             shard_id = shard_data.get(uid, 0)
#             if not shard_id:
#                 continue
#             if uid == tuid:
#                 continue
#             if (uid, tuid) in frd_lst:
#                 frd_shard_placeholds = frd_bind_placeholds.setdefault(shard_id, [])
#                 frd_shard_values = frd_values.setdefault(shard_id, [])
#                 inter_block['relation_type'] = USER_RELATION_INFO.FRD_INTER_BLOCK
#                 frd_shard_values.extend([inter_block[s_col] for s_col in columns])
#                 frd_shard_placeholds.append('(' + ','.join(['%s' for _ in columns]) + ')')
#             else:
#                 stranger_shard_placeholds = stranger_bind_placeholds.setdefault(shard_id, [])
#                 stranger_shard_values = stranger_values.setdefault(shard_id, [])
#                 inter_block['relation_type'] = USER_RELATION_INFO.STRANGER_INTER_BLOCK
#                 stranger_shard_values.extend([inter_block[s_col] for s_col in columns])
#                 stranger_shard_placeholds.append('(' + ','.join(['%s' for _ in columns]) + ')')
#             insert_uids.append((uid, tuid))
#         inter_block_data = [{'bind_placeholds': frd_bind_placeholds, 'values': frd_values},
#                             {'bind_placeholds': stranger_bind_placeholds, 'values': stranger_values}, ]
#         for data in inter_block_data:
#             values_data = data['values']
#             _bind_placeholds = data['bind_placeholds']
#             for shard_id, _values in values_data.iteritems():
#                 shard = PG_CONNS[shard_id]
#                 sql = 'INSERT INTO pw_relation_new ' + '(' + ','.join(columns) + ') VALUES ' + ','.join(
#                     _bind_placeholds[shard_id])
#                 sql = sql % tuple(_values)
#                 shard.execute(sql)
#                 shard.fetchall()
#         existed_relations.update(insert_uids)
#
#
# def sync_frd_block(block_lst, columns, frd_lst, shard_data, existed_relations):
#     pieces = split_list(block_lst)
#     for piece in pieces:
#         frd_block_bind_placeholds = {}
#         frd_block_values = {}
#         frd_blocked_bind_placeholds = {}
#         frd_blocked_values = {}
#         stranger_block_bind_placeholds = {}
#         stranger_block_values = {}
#         stranger_blocked_bind_placeholds = {}
#         stranger_blocked_values = {}
#
#         insert_uids = []
#         for block in piece:
#             uid = block['uid']
#             tuid = block['tuid']
#             block_shard_id = shard_data.get(uid, 0)
#             blocked_shard_id = shard_data.get(tuid, 0)
#             if not block_shard_id or not blocked_shard_id:
#                 continue
#             if (uid, tuid) in insert_uids:
#                 continue
#             if (tuid, uid) in insert_uids:
#                 continue
#             if uid == tuid:
#                 continue
#
#             block_shard_values = None
#             block_shard_placeholds = None
#             blocked_shard_values = None
#             blocked_shard_placeholds = None
#             block_relation_type = 0
#             blocked_relation_type = 0
#
#             if (uid, tuid) in frd_lst:
#                 block_shard_placeholds = frd_block_bind_placeholds.setdefault(block_shard_id, [])
#                 block_shard_values = frd_block_values.setdefault(block_shard_id, [])
#                 block_relation_type = USER_RELATION_INFO.FRD_BLOCK
#                 blocked_shard_placeholds = frd_blocked_bind_placeholds.setdefault(blocked_shard_id, [])
#                 blocked_shard_values = frd_blocked_values.setdefault(blocked_shard_id, [])
#                 blocked_relation_type = USER_RELATION_INFO.FRD_BLOCKED
#             else:
#                 block_shard_placeholds = stranger_block_bind_placeholds.setdefault(block_shard_id, [])
#                 block_shard_values = stranger_block_values.setdefault(block_shard_id, [])
#                 block_relation_type = USER_RELATION_INFO.STRANGER_BLOCK
#                 blocked_shard_placeholds = stranger_blocked_bind_placeholds.setdefault(blocked_shard_id, [])
#                 blocked_shard_values = stranger_blocked_values.setdefault(blocked_shard_id, [])
#                 blocked_relation_type = USER_RELATION_INFO.STRANGER_BLOCKED
#             insert_uids.append((uid, tuid))
#             insert_uids.append((tuid, uid))
#             block['relation_type'] = block_relation_type
#             block_shard_values.extend([block[s_col] for s_col in columns])
#             block_shard_placeholds.append('(' + ','.join(['%s' for _ in columns]) + ')')
#
#             blocked = {'uid': tuid, 'tuid': uid, 'relation_type': blocked_relation_type}
#             blocked['update_time'] = block['update_time']
#             blocked_shard_values.extend([blocked[s_col] for s_col in columns])
#             blocked_shard_placeholds.append('(' + ','.join(['%s' for _ in columns]) + ')')
#         block_data = [{'bind_placeholds': frd_block_bind_placeholds, 'values': frd_block_values},
#                       {'bind_placeholds': stranger_block_bind_placeholds, 'values': stranger_block_values},
#                       {'bind_placeholds': frd_blocked_bind_placeholds, 'values': frd_blocked_values},
#                       {'bind_placeholds': stranger_blocked_bind_placeholds, 'values': stranger_blocked_values}, ]
#         for data in block_data:
#             _bind_placeholds = data['bind_placeholds']
#             values = data['values']
#             for shard_id, _bind_placeholds in _bind_placeholds.iteritems():
#                 shard = PG_CONNS[shard_id]
#                 _values = values[shard_id]
#                 sql = 'INSERT INTO pw_relation_new ' + '(' + ','.join(columns) + ') VALUES ' + ','.join(
#                     _bind_placeholds[shard_id])
#                 sql = sql % tuple(_values)
#                 shard.execute(sql)
#                 shard.fetchall()
#         existed_relations.update(insert_uids)
#
#
# def sync_frds_data(frds_data, shard_data, existed_relations):
#     logging.info('sync_user_relation__ sync_frds start...')
#     begin = time.time()
#     columns = ['uid', 'tuid', 'relation_type', 'update_time', ]
#     pieces = split_list(frds_data)
#     idx = 0
#     for piece in pieces:
#         _begin = time.time()
#         shard_bind_placeholds = {}
#         shard_values = {}
#         insert_uids = []
#         for _data in piece:
#             uid = _data['uid']
#             tuid = _data['tuid']
#             if (uid, tuid) in existed_relations:
#                 continue
#             if (uid, tuid) in insert_uids:
#                 continue
#             if uid == tuid:
#                 continue
#             shard_id = shard_data.get(uid, 0)
#             if not shard_id:
#                 continue
#             insert_uids.append((uid, tuid))
#             _bind_place_holds = shard_bind_placeholds.setdefault(shard_id, [])
#             _values = shard_values.setdefault(shard_id, [])
#             relation_type = USER_RELATION_INFO.FRIEND
#             _data['relation_type'] = relation_type
#             _data['update_time'] = _data['create_time']
#             _values.extend([_data[s_col] for s_col in columns])
#             _bind_place_holds.append('(' + ','.join(['%s' for _ in columns]) + ')')
#         for shard_id, _bind_placeholds in shard_bind_placeholds.iteritems():
#             shard = PG_CONNS[shard_id]
#             _values = shard_values[shard_id]
#             sql = 'INSERT INTO pw_relation_new ' + '(' + ','.join(columns) + ') VALUES ' + ','.join(
#                 _bind_placeholds[shard_id])
#             sql = sql % tuple(_values)
#             shard.execute(sql)
#             shard.fetchall()
#         logging.info('sync_user_relation__ sync_frds {}, frds:{} {}, runtime:{}'.format(
#             idx, len(piece), piece[:10], time.time() - _begin))
#         existed_relations.update(insert_uids)
#
#     logging.info('sync_user_relation__ sync_frds end, runtime:{}'.format(time.time() - begin))
#
#
# def sync_contact_req_data(contact_req, shard_data, existed_relations):
#     columns = ['uid', 'tuid', 'relation_type', 'update_time', ]
#     begin = time.time()
#     logging.info('sync_user_relation__ sync_contact_req start...')
#     pieces = split_list(contact_req)
#     idx = 0
#     for piece in pieces:
#         _begin = time.time()
#         logging.info('sync_user_relation__ sync_contact_req, piece:{} {}'.format(len(piece), piece[:10]))
#         like_bind_placeholds = {}
#         like_values = {}
#         liked_bind_placeholds = {}
#         liked_values = {}
#         insert_uids = []
#         for each_data in piece:
#             uid = each_data['uid']
#             tuid = each_data['tuid']
#             if (uid, tuid) in existed_relations:
#                 continue
#             if uid == tuid:
#                 continue
#             if (uid, tuid) in insert_uids:
#                 continue
#             if (tuid, uid) in insert_uids:
#                 continue
#             like_shard_id = shard_data.get(uid, 0)
#             if not like_shard_id:
#                 continue
#             liked_shard_id = shard_data.get(tuid, 0)
#             if not liked_shard_id:
#                 continue
#             insert_uids.append((uid, tuid))
#             insert_uids.append((tuid, uid))
#             each_data['relation_type'] = USER_RELATION_INFO.LIKE
#             like_shard_placeholds = like_bind_placeholds.setdefault(like_shard_id, [])
#             like_shard_values = like_values.setdefault(like_shard_id, [])
#             like_shard_values.extend([each_data[s_col] for s_col in columns])
#             like_shard_placeholds.append('(' + ','.join(['%s' for _ in columns]) + ')')
#
#             liked_data = {'uid': tuid, 'tuid': uid, 'update_time': each_data['update_time'],
#                           'relation_type': USER_RELATION_INFO.LIKED}
#             liked_shard_placeholds = liked_bind_placeholds.setdefault(liked_shard_id, [])
#             liked_shard_values = liked_values.setdefault(liked_shard_id, [])
#             liked_shard_values.extend([liked_data[s_col] for s_col in columns])
#             liked_shard_placeholds.append('(' + ','.join(['%s' for _ in columns]) + ')')
#         contact_req_data = [{'bind_placeholds': like_bind_placeholds, 'values': like_values},
#                             {'bind_placeholds': liked_bind_placeholds, 'values': liked_values}, ]
#         for _contact_req_data in contact_req_data:
#             bind_placeholds = _contact_req_data['bind_placeholds']
#             values = _contact_req_data['values']
#             for shard_id, _bind_placeholds in bind_placeholds.iteritems():
#                 shard = PG_CONNS[shard_id]
#                 _values = values[shard_id]
#                 sql = 'INSERT INTO pw_relation_new ' + '(' + ','.join(columns) + ') VALUES ' + ','.join(
#                     _bind_placeholds[shard_id])
#                 sql = sql % tuple(_values)
#                 shard.execute(sql)
#                 shard.fetchall()
#         logging.info('sync_user_relation__ sync_contact_req {},  reqs:{} {}, runtime:{}'.format(
#             idx, len(piece), piece[:10], time.time() - _begin))
#         idx += 1
#         existed_relations.update(insert_uids)
#     logging.info('sync_user_relation__ sync_contact_erq end, runtime:{}'.format(time.time() - begin))
#
#
# def close():
#     for shard_id, pg_cursor in PG_CONNS.iteritems():
#         pg_cursor.close()
#         print shard_id, pg_cursor


if __name__ == '__main__':
    # sync_user_relations()
    # close()
    get_all_block_data()
