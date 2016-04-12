#!/usr/bin/env python
# coding: utf-8

import datetime
import random
import json

from django.conf import settings
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import UploadedFile, InMemoryUploadedFile, TemporaryUploadedFile
from django.core.files import File
from django.core.files.images import ImageFile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from spider.models import Movie
from coffin.shortcuts import render as coffin_render


# ------------------------------------------------------------------------------------
# 设置环境变量: sys.path(Initialized from the environment variable PYTHONPATH)
import sys
sys.path.append('/home/workspace/medusa/medusalib')
# ------------------------------------------------------------------------------------




class Jinja2View(View):
    """
    使用 Jinja2 模板
    """
    def get(self, request, *args, **kwargs):
        context = {}
        context.update(coffin_version='0.4.0')
        context.update(none_value=None)
        # print context
        # {'coffin_version': '0.4.0', 'none_value': None}
        # 跟 Django 模板不同，Jinja2 模板会将 None 显示为字符串 "None"
        return coffin_render(request, 'jinja2.html', context)




class MovieView_DB(View):
    """
    豆瓣电影 TOP250
    """
    def get(self, request, *args, **kwargs):
        """
        搜索 PostgreSQL
        """
        # 关键字参数和分页参数
        keyword = request.GET.get('keyword')
        page = request.GET.get('page', 1)
        # 查询数据库(数据来自spider)
        movies = Movie.objects.order_by('rank')
        if keyword:
            strict = Q(title__icontains=keyword) | \
                     Q(desc__icontains=keyword) | \
                     Q(quote__icontains=keyword)
            movies = movies.filter(strict)
            pass
        # 分页
        paginator = Paginator(object_list=movies, per_page=10)
        try:
            pager = paginator.page(page)
        except PageNotAnInteger:
            pager = paginator.page(1)
        except EmptyPage:
            pager = paginator.page(paginator.num_pages)
            pass
        # 分页片段中使用 pager.queries 达到在翻页时带着查询参数的目的
        pager.queries = "keyword=%s" % (request.GET.get('keyword') or '',)
        # [网页模板]和[通用分页片段(pagination_jinja.html)]中使用 "page" 来访问 Page object
        context = {}
        context['page'] = pager
        return coffin_render(request, 'movie.html', context)




class MovieView_ES(View):
    """
    豆瓣电影 TOP250
    """
    def get(self, request, *args, **kwargs):
        """
        搜索 ElasticSearch
        """
        # 关键字参数和分页参数
        keyword = request.GET.get('keyword')
        page = request.GET.get('page', 1)
        print '----------------------------------------------------------------------------------------'
        dsl_movie = {
            'query': {
                'bool': {
                    'should': [
                        {
                            'match': {
                                'title': keyword,
                            }
                        },
                        {
                            'match': {
                                'desc': keyword,
                            }
                        },
                        {
                            'match': {
                                'quote': keyword,
                            }
                        }
                    ]
                }
            }
        }
        # [1] 创建客户端对象 查询ElasticSearch
        # from pyelasticsearch import ElasticSearch
        # es = ElasticSearch(
        #     urls='http://192.168.100.100',
        #     port=9200,
        # )
        # [2] ElasticSearch(单例模式)
        from elasticsearchclient.elasticsearchclient import es_client
        print '>>>>>>>>>> ElasticSearch(Singleton)'
        print id(es_client)
        print '>>>>>>>>>> ElasticSearch(Singleton)'
        # ElasticSearch 分页参数: es_from, size
        search = es_client.search(
            index='douban',
            doc_type='movie',
            query=dsl_movie,
            es_from=0,
            size=250,
        )
        # print json.JSONEncoder(indent=4).encode(search)
        hits = search['hits']['hits']
        movies = [hit['_source'] for hit in hits]
        print '----------------------------------------------------------------------------------------'
        # 分页
        paginator = Paginator(object_list=movies, per_page=10)
        try:
            pager = paginator.page(page)
        except PageNotAnInteger:
            pager = paginator.page(1)
        except EmptyPage:
            pager = paginator.page(paginator.num_pages)
            pass
        # 分页片段中使用 pager.queries 达到在翻页时带着查询参数的目的
        pager.queries = "keyword=%s" % (request.GET.get('keyword') or '',)
        # [网页模板]和[通用分页片段(pagination_jinja.html)]中使用 "page" 来访问 Page object
        context = {}
        context['page'] = pager
        return coffin_render(request, 'movie.html', context)




class ES_Search(View):
    """
    ElasticSearch 搜索服务
    """
    def get(self, request, *args, **kwargs):
        # 接收 DSL 参数执行搜索
        dsl = request.GET.get('dsl')  # <type 'unicode'>
        dsl = json.loads(dsl)  # <type 'dict'>
        # ElasticSearch(单例模式)
        from elasticsearchclient.elasticsearchclient import es_client
        print '>>>>>>>>>> ElasticSearch(Singleton)'
        print id(es_client)
        print '>>>>>>>>>> ElasticSearch(Singleton)'
        search = es_client.search(
            index='douban',
            doc_type='movie',
            query=dsl,
            es_from=0,
            size=250,
        )  # <type 'dict'>
        ret = json.JSONEncoder(indent=4).encode(search)  # <type 'str'>
        print '----------------------------------------------------------------------------------------'
        print type(dsl)
        print dsl
        print '----------------------------------------------------------------------------------------'
        print type(ret)
        print ret
        print '----------------------------------------------------------------------------------------'
        return HttpResponse(content=ret, content_type='application/json; charset=UTF-8')




class RedisView(View):
    """
    Redis (singleton)
    """
    def get(self, request, *args, **kwargs):
        """
        Python的模块(module)，就是最 pythonic 的 singleton 典范。
        模块在在一个应用程序中只有一份，它本身就是单例的。
        所以只要将所需要的属性和方法，直接暴露在模块中变成模块的全局变量和全局方法即可！
        """
        from redisclient.redisclient import redis_db
        print '>>>>>>>>>> StrictRedis(Singleton)'
        print id(redis_db)
        print '>>>>>>>>>> StrictRedis(Singleton)'
        ret = 'redis_client_id: %s' % id(redis_db)
        return HttpResponse(ret)




from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
class PageCacheView(View):
    """
    Django Cache (PageCache)
    """
    @method_decorator(cache_page(3))
    def get(self, request, *args, **kwargs):
        ret = random.random()
        return HttpResponse(ret)


from django.core.cache import get_cache
class CustomCacheView(View):
    """
    Django Cache (CustomCache)
    """
    def get(self, request, *args, **kwargs):
        cache = get_cache('default')
        ret = cache.get('rand')
        if not ret:
            ret = random.random()
            cache.set('rand', ret, 3)
        return HttpResponse(ret)
