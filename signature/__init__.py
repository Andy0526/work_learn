# -*- coding: utf-8 -*-
import logging
import urllib
import urllib2
import json
import time

OAUTH2_API = 'https://login.vmall.com/oauth2/token'
PUSH_API = 'https://api.push.hicloud.com/pushsend.do?'


def push_message(payload):
    nsp_ctx = {"ver": "1", "appId": "10196688"}
    url = PUSH_API + urllib.urlencode({'nsp_ctx': nsp_ctx}).lower()
    params = dict(accessToken=get_access_token(), nsp_svc='openpush.message.api.send', nsp_ts=int(time.time()),
                  deviceTokens=json.dumps(['0867981022341500000000303400CN01']), payload=payload)
    print url
    request_url(url, **params)


def request_url(url, **params):
    data = urllib.urlencode(params)
    req = urllib2.Request(url, data=data)
    resp = urllib2.urlopen(req, timeout=5).read()
    result = json.loads(resp)
    logging.info('huawei_push request_url, url:{}, params:{}, result:{}'.format(url, params, result))
    return result


def get_access_token():
    params = {
        'grant_type': 'client_credentials',
        'client_id': '10196688',
        'client_secret': 'mivbs6gd0eaaq0haav6fodlc5g165ezp'
    }
    query = urllib.urlencode(params)
    req = urllib2.Request(OAUTH2_API, query)
    resp = urllib2.urlopen(req, timeout=5).read()
    data = json.loads(resp)
    return data['access_token']


def _push_huawei_android(content):
    """
    华为推动android
    :param bind:
    :param content:
    :param kwargs:
    :return:
    """
    body = dict(content=content, title='陪我')
    msg = dict(type=3, body=json.dumps(body))
    hps = dict(msg=json.dumps(msg))
    payload = dict(hps=json.dumps(hps))
    push_message(payload)


if __name__ == '__main__':
    _push_huawei_android('fuchangfuchang')
