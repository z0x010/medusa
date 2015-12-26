# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

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

class MedusaspiderPipeline(object):
    def process_item(self, item, spider):
        return item


"""
After an item has been scraped by a spider, it is sent to the Item Pipeline
which processes it through several components that are executed sequentially.
"""
from scrapy.exceptions import DropItem
class MovieSpiderPipeline(object):
    """
    Each item pipeline component (sometimes referred as just “Item Pipeline”) is a Python class
    that implements a simple method: process_item(self, item, spider)
    They receive an item and perform an action over it,
    also deciding if the item should continue through the pipeline or be dropped and no longer processed.
    """

    def __init__(self):
        # ------------------------------------------------------------------------------------
        # # 设置环境变量: sys.path(Initialized from the environment variable PYTHONPATH)
        # import sys
        # sys.path.append('/home/workspace/medusa')
        # # 设置 Django settings
        # from django.core.management import setup_environ
        # from medusaweb import settings as django_settings
        # setup_environ(django_settings)
        # # 使用 Django ORM
        # from medusaweb.spider.models import Movie
        # <class 'medusaweb.spider.models.Movie'>
        # self.model = Movie
        # ------------------------------------------------------------------------------------
        pass

    @classmethod
    def from_crawler(cls, crawler):
        """
        If present, this classmethod is called to create a pipeline instance from a Crawler.
        It must return a new instance of the pipeline.
        Crawler object provides access to all Scrapy core components like settings and signals;
        it is a way for pipeline to access them and hook its functionality into Scrapy.

        Parameters:
        crawler (Crawler object) – crawler that uses this pipeline
        """
        return cls()

    def open_spider(self, spider):
        """
        This method is called when the spider is opened.
            Parameters:	spider (Spider object) – the spider which was opened
        """
        print '[open_spider]', Movie.objects.count()
        pass

    def close_spider(self, spider):
        """
        This method is called when the spider is closed.
            Parameters:	spider (Spider object) – the spider which was closed
        """
        print '[close_spider]', Movie.objects.count()
        pass

    def process_item(self, item, spider):
        """
        This method is called for every item pipeline component and must
        either:
            return a dict with data, Item (or any descendant class) object
        or:
            raise a DropItem exception.
            Dropped items are no longer processed by further pipeline components.
        """
        print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> in process_item()'
        # 只取 rank 值小于等于100的 item
        if int(item['rank']) <= 250:
            print '[++++++++++][selected]', item['rank']
            print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [Write item to DB][start]'
            # print item
            # print dict(item)
            # (1)
            # movie = Movie(**item)
            # movie.save()
            # (2)
            Movie.objects.create(**item)
            print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [Write item to DB][stop]'
            return item
        else:
            print '[----------][dropped]', item['rank']
            raise DropItem("missing rank in %s" % item)
