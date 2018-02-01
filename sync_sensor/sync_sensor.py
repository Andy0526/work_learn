# -*- coding: utf-8 -*-
import threading
import psycopg2
import sys
import logging
import sensorsanalytics

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
    def query(self, sql):
        try:
            cur = self.read_conn.cursor(cursor_factory=RealDictCursor)
            cur.execute(sql)
            rs = cur.fetchall()
            self.read_conn.commit()
        except OperationalError:
            exc_class, exception, tb = sys.exc_info()
            raise exc_class, exception, tb
        finally:
            cur.close()
        return rs

    def close_all(self):
        self.read_conn.close()


db = DBStore()


class Sensor(object):
    SA_SERVER_URL = 'http://39.106.147.114:8106/sa?project=peiwo_sensor_test_data'
    SA = None

    @classmethod
    def init_sensor(cls, **kwargs):
        """
        初始化连接
        :param kwargs:
        :return:
        """
        consumer = sensorsanalytics.DefaultConsumer(cls.SA_SERVER_URL, 800)
        cls.SA = sensorsanalytics.SensorsAnalytics(consumer)

    @classmethod
    def profile_set(cls, uid, properties, is_login_id=True):
        try:
            if not cls.SA:
                cls.init_sensor()
            cls.SA.profile_set(str(uid), properties, is_login_id=is_login_id)
        except Exception as e:
            logging.error("sensor error profile_set %s " % e)

    @classmethod
    def close(cls):
        """
        关闭连接
        :return:
        """
        cls.SA.close()


def sync_user_profile():
    while True:
        sql = 'select * from user_pays_lives order by uid limit 5000'
        results = db.query(sql)
        for res in results:
            print res
            uid = res.pop('uid')
            Sensor.profile_set(uid, res)


if __name__ == '__main__':
    sync_user_profile()
    db.read_conn.close()
    Sensor.close()
