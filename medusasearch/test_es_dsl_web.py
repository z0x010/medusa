#!/usr/bin/env python
# coding:utf-8

"""
请求 ElasticSearch web service 获取搜索结果
"""

import json
import requests


def es_search(es_dsl):
    response = requests.get(url='http://192.168.100.100:8000/es/search/', params={'dsl': json.dumps(es_dsl)})
    # ret = response.json()  # <type 'dict'>
    # ret = response.text  # <type 'unicode'>
    # ret = response.content  # <type 'str'>
    return response.content


# ----------------------------------------------------------------------------------------
dsl = {
    'query': {
        'match': {
            'rank': 1
        }
    }
}
# ----------------------------------------------------------------------------------------
ret = es_search(dsl)
print ret
