# coding: utf-8

import scrapy
import re
from medusaspider.items import MovieItem


class NewsSpider(scrapy.spiders.Spider):
    name = 'movie_spider'
    start_urls = [
        "http://movie.douban.com/top250",
    ]

    def parse(self, response):
        print '-----------------------------------------------------------------------------------'
        print response
        # print response.body
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
        for selector in response.xpath('//ol[@class="grid_view"]/li/div[@class="item"]'):
            # print selector
            rank = selector.xpath('div[@class="pic"]/em/text()').extract()[0]
            pic = selector.xpath('div[@class="pic"]/a/img/@src').extract()[0]
            title_list = selector.xpath('div[@class="info"]/div[@class="hd"]/a/span[@class="title"]/text()').extract()
            title = ''.join([title.encode('utf-8') for title in title_list])
            url = selector.xpath('div[@class="info"]/div[@class="hd"]/a/@href').extract()[0]
            desc_list = selector.xpath('div[@class="info"]/div[@class="bd"]/p/text()').extract()
            desc = ''.join(desc.encode('utf-8') for desc in desc_list)
            star_class = selector.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/@class').extract()[0]
            star = int(star_class.replace('rating', '').replace('-t', ''))
            star = float(star) if 0 <= star <= 5 else star/10.0
            rate = selector.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            comment_span = selector.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span').extract()[3]
            comment = int(re.findall('\d+', comment_span)[0])
            quote = selector.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()').extract()[0].encode('utf-8')

            print rank
            print pic
            print title
            print url
            print desc
            print star
            print rate
            print comment
            print quote

            pass
        print '-----------------------------------------------------------------------------------'
        pass
    pass
