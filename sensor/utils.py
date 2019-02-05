# -*- coding: utf-8 -*-

import requests
import json

# from sensor.const import SENSOR_API_URL, SENSOR_TOKEN, SENSOR_PROJECT

SENSOR_API_URL = 'http://39.106.147.114:8107/api/'
SENSOR_PROJECT = 'peiwo_sensor_test_data'
SENSOR_TOKEN = '8e8622d0a97677a819e15fcec7b92002a66d2dc2a7de1feae9a47b80d79a668c'

def sql_query(sql):
    payload = dict(
        project=SENSOR_PROJECT,
        token=SENSOR_TOKEN,
        q=sql,
        format='json')
    url = SENSOR_API_URL + '/sql/query'
    response = requests.post(url, params=payload)
    return format_response(response)


def format_response(response):
    results = []
    res_list = str(response.content).split('\n')
    print res_list
    for line in res_list:
        line = line.strip()
        if line:
            results.append(json.loads(line))
    return results


if __name__ == '__main__':
    data = sql_query(
        "select distinct_id from events where $ip like '106.117.14%' and  time >'2018-05-22 14:30:00' group by distinct_id order by length(distinct_id)")
    print len(data)
