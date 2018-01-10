#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

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
    mongo_uri = '192.168.100.2:22000'
    pg_master = 'dbname=sneaky user=sneaky password=77WN88wwc host=192.168.100.1'
    pg_shard = {
        1: 'dbname=sneaky user=sneaky password=77WN88wwc host=192.168.100.1',
        2: 'dbname=sneaky user=sneaky password=77WN88wwc host=192.168.100.21',
    }


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
