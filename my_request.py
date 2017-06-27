#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

import requests
import json


def get_response(url, method='get', headers=None, params=None):
    if not url:
        return None
    request_func = requests.get
    if method == 'post':
        request_func = requests.post
    # proxies = {
    #     "http": "http://121.232.147.143:9000",
    #     "https": "http://121.232.147.143:9000",
    # }
    response = request_func(url=url, headers=headers, params=params)
    return response


if __name__ == '__main__':
    url = 'https://api.raybo.com:2443/v1.0/live/sum_total?uid=76954422&cursor=&t=1497579392848&extra=dadadadadadadda'
    headers = {"x-forwarded-for": '137.123.78.123:8989'}
    res = get_response(url, headers=headers)
    print res.content

    print json.loads(res.content)
