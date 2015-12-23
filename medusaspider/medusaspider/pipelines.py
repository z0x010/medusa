# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


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
    # def process_item(self, item, spider):
    #     """
    #     This method is called for every item pipeline component and must
    #     either:
    #         return a dict with data, Item (or any descendant class) object
    #     or:
    #         raise a DropItem exception.
    #         Dropped items are no longer processed by further pipeline components.
    #     """
    #     print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> in process_item()'
    #     print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [Write item to DB][start]'
    #     # print item
    #     # print spider
    #     print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [Write item to DB][stop]'
    #     return item

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
        if int(item['rank']) <= 100:
            print '[++++++++++][selected]', item['rank']
            return item
        else:
            print '[----------][dropped]', item['rank']
            raise DropItem("missing rank in %s" % item)

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
