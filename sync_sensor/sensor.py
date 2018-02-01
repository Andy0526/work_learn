# -*- coding: utf-8 -*-
import logging
import sensorsanalytics
from datetime import datetime


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
