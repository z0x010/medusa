#!/usr/bin/env python
# coding:utf-8


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

from pyelasticsearch import ElasticSearch
es = ElasticSearch('http://192.168.100.100:9200')
# <pyelasticsearch.client.ElasticSearch object at 0x1c86a90>

print '------------------------------------------------------------------------------------'
################################################################################ [1] index
# index = es.bulk_index(index='douban', doc_type='movie', docs=docs_movies)
# print index
# {
#   u'items': [
#     {
#       u'index': {
#         u'status': 200,
#         u'_type': u'movie',
#         u'_id': u'451',
#         u'_version': 2,
#         u'_index': u'douban'
#       }
#     },
#     {
#       u'index': {
#         u'status': 200,
#         u'_type': u'movie',
#         u'_id': u'452',
#         u'_version': 2,
#         u'_index': u'douban'
#       }
#     },
#     {
#       u'index': {
#         u'status': 200,
#         u'_type': u'movie',
#         u'_id': u'453',
#         u'_version': 2,
#         u'_index': u'douban'
#       }
#     },
#   ],
#   u'errors': False,
#   u'took': 1173
# }

################################################################################ [2] refresh
# refresh = es.refresh(index='douban')
# print refresh
# {u'_shards': {u'successful': 5, u'failed': 0, u'total': 10}}

################################################################################ [3] get
get = es.get(index='douban', doc_type='movie', id=455)
print get
# {
#   u'_type': u'movie',
#   u'_source': {
#     u'comment': 126681,
#     u'star': 4.5,
#     u'title': u'\u8d85\u8131\xa0/\xa0Detachment',
#     u'url': u'http://movie.douban.com/subject/5322596/',
#     u'quote': u'...',
#     u'pic': u'http://img3.douban.com/view/movie_poster_cover/ipst/public/p1305562621.jpg',
#     u'rank': 101,
#     u'rate': 8.7,
#     u'desc': u'...'
#   },
#   u'_index': u'douban',
#   u'_version': 2,
#   u'found': True,
#   u'_id': u'455'
# }
print '------------------------------------------------------------------------------------'
