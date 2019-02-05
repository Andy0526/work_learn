# -*- coding: utf-8 -*-
import logging

from elasticsearch import Transport, Elasticsearch, NotFoundError
from elasticsearch.client import _normalize_hosts
from elasticsearch.helpers import bulk as smart_bulk


class ESO(object):
    INDEX = None
    TYPE = None

    @classmethod
    def query(cls, doc_type=None, body=None, **kwargs):
        doc_type = doc_type if doc_type else cls.TYPE
        result = ESearch.read.search(cls.INDEX, doc_type=doc_type, body=body, **kwargs)
        return result

    @classmethod
    def delete(cls, index=None):
        index = index if index else cls.INDEX
        result = ESearch.write.indices.delete(index=index)
        return result

    @classmethod
    def insert_many(cls, actions, stats_only=False, **kwargs):
        result = ESearch.write.batch(actions, stats_only, **kwargs)
        return result

    @classmethod
    def update(cls, body, id, doc_type=None, **kwargs):
        doc_type = doc_type if doc_type else cls.TYPE
        result = ESearch.write.update(
            index=cls.INDEX, doc_type=doc_type, id=id, body=body, **kwargs)
        return result


def normalize_hosts(hosts):
    """
      result: {w: {host:xxx, prot:xxx}, r: {}}
    """

    def _analyze(hosts):
        # hosts length is 2 at least
        az_hosts = {}
        if isinstance(hosts, dict):
            for k, h in hosts.iteritems():
                az_hosts[k] = _normalize_hosts(h)
        elif isinstance(hosts, list):
            az_hosts['r'] = _normalize_hosts(hosts[0])
            az_hosts['w'] = _normalize_hosts(hosts[1])

        return az_hosts

    if len(hosts) > 1:
        az_hosts = _analyze(hosts)
    else:
        host = hosts[0] if isinstance(hosts, list) else hosts.values[0]
        az_hosts = _analyze([host, host])

    return az_hosts


class ESBase(object):
    max_r_trans = 3

    def __init__(self):
        self.hosts = normalize_hosts(['172.16.10.189:9200'])
        self.w_host = self.hosts['w']
        self.r_host = self.hosts['r']
        self.write_transport = None
        self.read_transport = None

    def get_read_transport(self, **kwargs):
        if not self.read_transport:
            r_host = self.r_host if len(self.r_host) > 1 else self.r_host * self.max_r_trans
            self.read_transport = Transport(r_host, **kwargs)
        return self.read_transport

    def get_write_transport(self, **kwargs):
        if not self.write_transport:
            self.write_transport = Transport(self.w_host, **kwargs)
        return self.write_transport


class DummyESearch(Elasticsearch):

    def __init__(self, transport_ins):
        super(DummyESearch, self).__init__()
        # TODO: add attributes ``cat``, ``cluster``, ``indices``, ``nodes``
        # and ``snapshot`` that provide access to instances of each
        self.transport = transport_ins

    def batch(self, actions, stats_only=False, **kwargs):
        # override Elasticsearch bulk method, use helpers bulk
        result = smart_bulk(self, actions, stats_only, **kwargs)
        return result


class ESearch(object):
    base = ESBase()
    read = DummyESearch(base.get_read_transport(http_auth=('elastic', 'esraybo123')))
    write = DummyESearch(base.get_write_transport(http_auth=('elastic', 'esraybo123')))


class EsBriefSetting(ESO):
    INDEX = 'brief_setting'
    TYPE = 'standby'

    switch_names = {
        'user_brief_a': 'user_brief_b',
        'user_brief_b': 'user_brief_a'
    }

    _id = 1

    @classmethod
    def get_brief_name(cls):
        body = {
            'query': {
                'constant_score': {
                    'filter': {
                        'term': {
                            '_id': cls._id
                        }
                    }
                }
            }
        }

        try:
            result = cls.query(body=body)
        except NotFoundError as e:
            logging.warn('setting index not exists, please check! err=%s' % e)
            return cls.get_default_brief_name()

        hits = result['hits']
        if not hits.get('total'):
            logging.info('ESearch setting not exists!')
            return None
        else:
            return hits['hits'][0]['_source']['tp_name']

    @classmethod
    def get_default_brief_name(cls):
        # 缺省名
        default = cls.switch_names.values()[0]
        return default

    @classmethod
    def delete_idle_brief(cls, index=None):
        ops_index = index if index else cls.get_opposite_brief_name()
        result = None
        try:
            result = cls.delete(ops_index)
        except NotFoundError as e:
            logging.warn('Index not exists, name=%s, err=%s' % (ops_index, e))
        return result

    @classmethod
    def get_opposite_brief_name(cls):
        cur_name = cls.get_brief_name()
        ops_name = cls.switch_names[cur_name]
        return ops_name

    @classmethod
    def switch_brief_name(cls):
        used_name = cls.get_opposite_brief_name()
        body = {
            'doc': {
                'tp_name': used_name
            },
            'doc_as_upsert': True
        }
        result = cls.update(doc_type=cls.TYPE, id=cls._id, body=body)
        return result.get('result', '') == 'updated'


def setindex(func):
    def _wrap_func(cls, *args, **kwargs):
        index = EsBriefSetting.get_brief_name()
        if index == cls.INDEX:
            pass
        else:
            cls.INDEX = index
        ret = func(cls, *args, **kwargs)
        return ret

    return _wrap_func


class EsUserBrief(ESO):
    INDEX = 'user_brief_a'
    TYPE = 'briefs'

    @classmethod
    @setindex
    def query_users_by_name(cls, name, start=0, limit=10, return_keys=None):
        body = {
            'query': {
                'bool': {
                    'must': [
                        {
                            'term': {
                                'state': 1
                            }
                        },
                        {
                            'match': {
                                'name': {
                                    'query': name,
                                    'minimum_should_match': '100%'
                                }
                            }
                        },
                    ],
                    'should': {
                        'match_phrase': {
                            'name': {
                                'query': name,
                                'slop': 5
                            }
                        }
                    }
                }
            },
            'highlight': {
                'fields': {
                    'name': {}
                }
            },
            'sort': [
                # { "_score": { "order": "desc" }},
                {"liked_number": {"order": "desc"}}
            ]
        }

        result = []
        res = cls.query(body=body, params={'from': start, 'size': limit})

        hits = res.get('hits')
        if hits:
            hits = hits.get('hits')
            for each in hits:
                user = each['_source']
                if not user:
                    continue
                if isinstance(return_keys, (list, tuple)):
                    ned = {}
                    for k in return_keys:
                        if k in user:
                            ned[k] = user[k]
                else:
                    ned = user
                result.append(ned)

        return result


print EsUserBrief.query_users_by_name('蒜')
