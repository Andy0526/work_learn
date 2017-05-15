#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan
import random
import functools

import pymongo


class Mongo_DB(object):
    host = '172.16.10.130'
    port = 22000
    cli = None

    def __init__(self):
        try:
            self.cli = pymongo.MongoClient(self.host, self.port)
        except:
            import traceback
            print traceback.print_exc()

    def insert(self, db, table, info):
        try:
            table = self.cli[db][table]
            table.insert(info)
        except:
            import traceback
            print traceback.print_exc()


def prepare_location_data():
    locations = []
    for i in range(10):
        data = {}
        data['live_id'] = i
        data['geo'] = {'loc': [round(random.uniform(0, 90), 4) for _ in range(2)]}
        locations.append(data)
    return locations


def main():
    mongo = Mongo_DB()

    func_part = functools.partial(mongo.insert, 'sneaky', 'test_locate')
    for data in prepare_location_data():
        func_part(data)


if __name__ == '__main__':
    main()
