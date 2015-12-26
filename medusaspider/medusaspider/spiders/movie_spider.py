# coding: utf-8

"""
usage:
$ scrapy crawl movie_spider -o db.json
"""

import scrapy
import re
import inspect
from medusaspider.items import MovieItem


class MovieSpider(scrapy.spiders.Spider):
    """
    Spiders are classes that you define and Scrapy uses to scrape information from a domain (or group of domains).
    They define:
        [1] an initial list of URLs to download,
        [2] how to follow links,
        [3] how to parse the contents of pages to extract items.
    """

    # A string which defines the name for this spider.
    # The spider name is how the spider is located (and instantiated) by Scrapy, so it must be unique.
    # This is the most important spider attribute and it’s required.
    name = 'movie_spider'

    # A list of URLs where the spider will begin to crawl from, when no particular URLs are specified.
    # So, the first pages downloaded will be those listed here.
    # The subsequent URLs will be generated successively from data contained in the start URLs.
    start_urls = [
        "http://movie.douban.com/top250",
    ]

    def parse(self, response):
        """
        a callback method:
            [1] extract some items,
            [2] looks for a link to follow to the next page, and then yields a Request with a callback for it;
        """
        # print response
        # print response.headers
        # print response.body
        # print response.meta
        # print response.selector
        # print dir(response)
        # print inspect.getmembers(response)

        """ [1][extract data from the page]
        """
        for selector in response.selector.xpath('//ol[@class="grid_view"]/li/div[@class="item"]'):
            # response.selector.xpath():
            # returns a list of selectors, each of which represents the node selected by the xpath expression.
            print '↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ (in parse)'
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

            item = MovieItem()
            item['rank'] = rank
            item['pic'] = pic
            item['title'] = title
            item['url'] = url
            item['desc'] = desc
            item['star'] = star
            item['rate'] = rate
            item['comment'] = comment
            item['quote'] = quote
            print '↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ (in parse)'
            yield item

        """ [2][extract links from the page, follow them, and then extract data from the pages]
        """
        print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
        next_page = response.xpath('//span[@class="next"]/a/@href').extract()
        # [u'?start=200&filter=']
        if next_page:
            next_url = response.urljoin(next_page[0])
            # http://movie.douban.com/top250?start=25&filter=

            # Scrapy’s mechanism of following links:
            # when you yield a Request in a callback method,
            # Scrapy will schedule that request to be sent,
            # and register a callback method to be executed when that request finishes.

            # This creates a sort of loop,
            # following all the links to the next page until it doesn’t find one
            # – handy for crawling blogs, forums and other sites with pagination.
            yield scrapy.Request(next_url, self.parse)
        print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
