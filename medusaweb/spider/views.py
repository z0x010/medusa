#!/usr/bin/env python
# coding: utf-8

import datetime
import random

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


from coffin.shortcuts import render as coffin_render
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


from spider.models import Movie
class MovieView(View):
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

    def post(self, request, *args, **kwargs):
        """
        搜索 ElasticSearch
        """
        # 关键字参数和分页参数
        keyword = request.GET.get('keyword')
        page = request.GET.get('page', 1)
        print '--------------------------------------------------'
        # 查询 ElasticSearch
        movies = []
        print '--------------------------------------------------'
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
