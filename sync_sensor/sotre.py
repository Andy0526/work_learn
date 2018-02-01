# -*- coding: utf-8 -*-
import threading
import psycopg2
import sys

from psycopg2._psycopg import DatabaseError, OperationalError
from psycopg2.extras import RealDictCursor


class DBStore(object):
    """
    数据库连接池
    """

    def __init__(self, retry=1):
        # 线程锁保证原子操作
        self.retry = retry
        self.lock = threading.Lock()
        self.read_conn = self.conn('dbname=sneaky user=sneaky password=sneaky host=192.168.100.111')

    def conn(self, params):
        conn = psycopg2.connect(params)
        return conn

    def execute_retry(func):  # noqa
        def call(self, *args, **kwargs):
            attempts = 0
            while True:
                self.lock.acquire()
                try:
                    return func(self, *args, **kwargs)
                except DatabaseError:
                    if attempts >= self.retry:
                        raise
                    attempts += 1
                finally:
                    self.lock.release()

        return call

    @execute_retry
    def query(self, sql, conn):
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute(sql)
            rs = cur.fetchall()
            conn.commit()
        except OperationalError:
            exc_class, exception, tb = sys.exc_info()
            raise exc_class, exception, tb
        finally:
            cur.close()
        return rs

    def close_all(self):
        self.read_conn.close()


db = DBStore()


def main():
    cur = db.read_conn.cursor()
    cur.execute('select * from pw_user limit 1')
    print cur.fetchall()


if __name__ == '__main__':
    main()
