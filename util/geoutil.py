#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan
import logging
import traceback
from geopy.distance import vincenty
from geopy.geocoders import Baidu
from geopy.exc import GeocoderTimedOut
from retrying import retry


def retry_if_timeout(exception):
    logging.error('geo_decode error! %s' % (traceback.format_exc()))
    return isinstance(exception, GeocoderTimedOut)


logging.basicConfig(level=logging.DEBUG, filename='geopy.log')


class GeoUtil(object):
    CHINA_SPECIAL = {
        u'香港特别行政区': 'HK',
        u'澳门特别行政区': 'MO',
        u'台湾省': 'TW'
    }
    Geolocator = Baidu('FDecb47114bb41c22f471828a4623800')
    FILE_NAME = 'country_code.dat'
    COUNTRY_CODE = {}

    @classmethod
    def init(cls):
        try:
            f = open(cls.FILE_NAME, 'r')
            for line in f:
                line = line.strip()
                if not len(line) or line.startswith('#'):
                    continue
                code = line.split(',')
                if len(code) >= 4:
                    cls.COUNTRY_CODE[int(code[1])] = {
                        'country': code[0],
                        'country_code': code[1],
                        'code': code[2],
                        'country_name': code[3]
                    }

            f.close()
        except:
            traceback.print_exc()

    @classmethod
    def distance(cls, f, t):
        if not f or not t:
            return -1

        try:
            f_location = [float(v) for v in f.split(',')]
            t_location = [float(v) for v in t.split(',')]
            return vincenty(f_location, t_location).km
        except:
            traceback.print_exc()
            return -1

    @classmethod
    @retry(stop_max_attempt_number=3, retry_on_exception=retry_if_timeout)
    def decode(cls, geo):
        # try:
        r = cls.Geolocator.reverse(geo)
        return r.raw.get('addressComponent')
        # except GeocoderTimedOut:
        #     logging.info('geo_decode error! geo:%s GeocoderTimedOut' % (geo,))
        # except:
        #     logging.error('geo_decode error! geo:%s %s' % (geo, traceback.format_exc()))

    # country, province, city
    @classmethod
    def get_locations(cls, geo):
        decode = cls.decode(geo)
        if not decode:
            return 'CN', '', ''

        c_code = decode.get('country_code')
        if c_code == 0:
            p = decode.get('province')
            if cls.CHINA_SPECIAL.get(p):
                return cls.CHINA_SPECIAL.get(p), decode.get('province'), decode.get('city')
            else:
                return 'CN', decode.get('province'), decode.get('city')
        elif cls.COUNTRY_CODE.get(c_code):
            return cls.COUNTRY_CODE.get(c_code)['code'], decode.get('province'), decode.get('city')
        else:
            # 显示其他
            return 'QT', decode.get('province'), decode.get('city')
