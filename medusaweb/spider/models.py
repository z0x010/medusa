# coding: utf-8

from django.db import models


class Movie(models.Model):
    rank = models.IntegerField(verbose_name=u'排名', null=True)
    pic = models.CharField(verbose_name=u'图片', null=True, max_length=200)
    title = models.CharField(verbose_name=u'标题', null=True, max_length=200)
    url = models.CharField(verbose_name=u'链接', null=True, max_length=200)
    desc = models.CharField(verbose_name=u'详情', null=True, max_length=500)
    star = models.DecimalField(verbose_name=u'星级', null=True, decimal_places=1, max_digits=2)
    rate = models.DecimalField(verbose_name=u'评分', null=True, decimal_places=1, max_digits=2)
    comment = models.IntegerField(verbose_name=u'评论', null=True)
    quote = models.CharField(verbose_name=u'描述', null=True, max_length=200)
