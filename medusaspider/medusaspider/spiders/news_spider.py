# coding: utf-8

import scrapy
from medusaspider.items import NewsItem


class NewsSpider(scrapy.spiders.Spider):
    name = 'news_spider'
    start_urls = [
        "http://m.toutiao.com/",
    ]

    def parse(self, response):
        print '-----------------------------------------------------------------------------------'
        print response
        # print dir(response)
        # print 'response.body', response.body
        # print 'response.body_as_unicode', response.body_as_unicode
        # print 'response.copy', response.copy
        # print 'response.css', response.css
        # print 'response.encoding', response.encoding
        # print 'response.flags', response.flags
        # print 'response.headers', response.headers
        # print 'response.meta', response.meta
        # print 'response.replace', response.replace
        # print 'response.request', response.request
        # print 'response.selector', response.selector
        # print 'response.status', response.status
        # print 'response.url', response.url
        # print 'response.urljoin', response.urljoin
        # print 'response.xpath', response.xpath
        print '-----------------------------------------------------------------------------------'
        pass

    pass
