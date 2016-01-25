#!/usr/bin/env python
# coding:utf-8


import json


# ------------------------------------------------------------------------------------
# 设置环境变量: sys.path(Initialized from the environment variable PYTHONPATH)
import sys
sys.path.append('/home/workspace/medusa')
# 设置 Django settings
from django.core.management import setup_environ
from medusaweb import settings as django_settings
setup_environ(django_settings)
# 使用 Django ORM
from medusaweb.spider.models import Movie
# <class 'medusaweb.spider.models.Movie'>
# ------------------------------------------------------------------------------------
# 读 django 数据库, 获取模型数据
docs_movies = Movie.objects.all().values()
# print docs_movies
# [
#   {
#     'comment': 64784,
#     'star': Decimal('4.5'),
#     'title': u'\u4e2d\u592e\u8f66\u7ad9\xa0/\xa0Central do Brasil',
#     'url': u'http://movie.douban.com/subject/1292218/',
#     'quote': u'\u5fc3\u7075\u6551\u8d4e\u3002',
#     'pic': u'http://img3.douban.com/view/movie_poster_cover/ipst/public/p2239441575.jpg',
#     'rank': 201,
#     'rate': Decimal('8.7'),
#     'id': 451,
#     'desc': u''
#   },
#   {
#     'comment': 146971,
#     'star': Decimal('4.5'),
#     'title': u'\u65e0\u654c\u7834\u574f\u738b\xa0/\xa0Wreck-It Ralph',
#     'url': u'http://movie.douban.com/subject/6534248/',
#     'quote': u'\u8fea\u58eb\u5c3c\u548c\u76ae\u514b\u65af\u62ff\u9519\u5267\u672c\u7684\u4ea7\u7269\u3002',
#     'pic': u'http://img4.douban.com/view/movie_poster_cover/ipst/public/p1735642656.jpg',
#     'rank': 226,
#     'rate': Decimal('8.7'),
#     'id': 452,
#     'desc': u''
#   },
#   ...
# ]
# ------------------------------------------------------------------------------------
print '============================================================================ ElasticSearch'
from pyelasticsearch import ElasticSearch
es = ElasticSearch('http://192.168.100.100:9200')
# <pyelasticsearch.client.ElasticSearch object at 0x1c86a90>

print '============================================================================ [1] create index'
# index = es.bulk_index(index='douban', doc_type='movie', docs=docs_movies)
# print json.JSONEncoder(indent=4).encode(index)
# {
#     "items": [
#         {
#             "index": {
#                 "status": 201,
#                 "_type": "movie",
#                 "_id": "451",
#                 "_version": 1,
#                 "_index": "douban"
#             }
#         },
#         {
#             "index": {
#                 "status": 201,
#                 "_type": "movie",
#                 "_id": "452",
#                 "_version": 1,
#                 "_index": "douban"
#             }
#         },
#         {
#             "index": {
#                 "status": 201,
#                 "_type": "movie",
#                 "_id": "453",
#                 "_version": 1,
#                 "_index": "douban"
#             }
#         },
#         ...
#     ],
#     "errors": false,
#     "took": 3557
# }
print '============================================================================ [2] delete index'
# delete = es.delete_index('douban')
# print json.JSONEncoder(indent=4).encode(delete)
# {
#     "acknowledged": true
# }
print '============================================================================ [3] refresh index'
# refresh = es.refresh(index='douban')
# print json.JSONEncoder(indent=4).encode(refresh)
# {
#     "_shards": {
#         "successful": 5,
#         "failed": 0,
#         "total": 10
#     }
# }
print '============================================================================ [4] get'
# get = es.get(index='douban', doc_type='movie', id=499)
# print json.JSONEncoder(indent=4).encode(get)
# {
#     "_type": "movie",
#     "_source": {
#         "comment": 141800,
#         "star": 4.5,
#         "title": "\u65b0\u9f99\u95e8\u5ba2\u6808\u00a0/\u00a0\u65b0\u9f8d\u9580\u5ba2\u68e7",
#         "url": "http://movie.douban.com/subject/1292287/",
#         "quote": "\u5b09\u7b11\u6012\u9a82\uff0c\u8c03\u98ce\u52a8\u6708\u3002",
#         "pic": "http://img3.doubanio.com/view/movie_poster_cover/ipst/public/p1421018669.jpg",
#         "rank": 209,
#         "rate": 8.4,
#         "desc": "..."
#     },
#     "_index": "douban",
#     "_version": 1,
#     "found": true,
#     "_id": "499"
# }
print '============================================================================ [5] search'
"""
??????????????????????????????????????????????????
Query DSL
??????????????????????????????????????????????????
"""
search = es.search(
    index='douban',
    doc_type='movie',
    query={
        'query': {
            "match_all": {}
        },
    },
)
print json.JSONEncoder(indent=4).encode(search)
# {
#     "hits": {
#         "hits": [
#             {
#                 "_score": 1.0,
#                 "_index": "douban"
#                 "_type": "movie",
#                 "_id": "453",
#                 "_source": {
#                     "comment": 660703,
#                     "star": 5.0,
#                     "title": "\u8096\u7533\u514b\u7684\u6551\u8d4e\u00a0/\u00a0The Shawshank Redemption",
#                     "url": "http://movie.douban.com/subject/1292052/",
#                     "quote": "\u5e0c\u671b\u8ba9\u4eba\u81ea\u7531\u3002",
#                     "pic": "http://img3.douban.com/view/movie_poster_cover/ipst/public/p480747492.jpg",
#                     "rank": 1,
#                     "rate": 9.6,
#                     "desc": "..."
#                 },
#             },
#             {
#                 "_score": 1.0,
#                 "_index": "douban"
#                 "_type": "movie",
#                 "_id": "460",
#                 "_source": {
#                     "comment": 44860,
#                     "star": 4.5,
#                     "title": "\u8fc1\u5f99\u7684\u9e1f\u00a0/\u00a0Le peuple migrateur",
#                     "url": "http://movie.douban.com/subject/1292281/",
#                     "quote": "\u6700\u7f8e\u7684\u98de\u7fd4\u3002",
#                     "pic": "http://img4.douban.com/view/movie_poster_cover/ipst/public/p2238274168.jpg",
#                     "rank": 152,
#                     "rate": 9.1,
#                     "desc": "..."
#                 },
#             },
#         ],
#         "total": 250,
#         "max_score": 1.0
#     },
#     "_shards": {
#         "successful": 5,
#         "failed": 0,
#         "total": 5
#     },
#     "took": 192,
#     "timed_out": false
# }
print '============================================================================'
