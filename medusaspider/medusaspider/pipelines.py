# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MedusaspiderPipeline(object):
    def process_item(self, item, spider):
        return item


from scrapy.exceptions import DropItem
class MovieSpiderPipeline(object):
    def process_item(self, item, spider):
        """
        每个item pipeline组件都需要调用该方法，
        这个方法必须返回一个 Item (或任何继承类)对象，
        或是抛出 DropItem 异常，被丢弃的item将不会被之后的pipeline组件所处理。
        """
        print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [Write item to DB][start]'
        # print item
        print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [Write item to DB][stop]'
        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    pass
