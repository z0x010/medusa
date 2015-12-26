# coding: utf-8

"""
usage:
$ scrapy crawl movie_crawlspider -o db.json
"""

import scrapy
import re
import inspect
from medusaspider.items import MovieItem


class MovieCrawlSpider(scrapy.spiders.CrawlSpider):
    """
    scrapy.spiders.CrawlSpider
        This is the most commonly used spider for crawling regular websites,
        as it provides a convenient mechanism for following links by defining a set of rules.
        It’s generic enough for several cases, you can start from it and override it
        as needed for more custom functionality, or just implement your own spider.
    """

    name = 'movie_crawlspider'

    start_urls = [
        "http://movie.douban.com/top250",
    ]

    # rules:
    # a list of one (or more) Rule objects.
    # Each Rule defines a certain behaviour for crawling the site.
    # If multiple rules match the same link, the first one will be used,
    # according to the order they’re defined in this attribute.
    rules = [
        scrapy.spiders.Rule(
            link_extractor=scrapy.linkextractors.LinkExtractor(
                allow=('top250.*',),
                deny=(),
            ),
            callback='parse_item',
        ),
    ]

    def parse_start_url(self, response):
        """
        This method is called for the start_urls responses.
        It allows to parse the initial responses and
        must return either an Item object, a Request object, or an iterable containing any of them.
        """
        return super(MovieCrawlSpider, self).parse_start_url(response)

    def parse_item(self, response):
        """
        Warning:
        When writing crawl spider rules, avoid using parse as callback,
        since the CrawlSpider uses the parse method itself to implement its logic.
        So if you override the parse method, the crawl spider will no longer work.
        """
        # [1][extract data from the page]
        # (A)(shortcut)
        # for selector in response.selector.xpath('//ol[@class="grid_view"]/li/div[@class="item"]'):
        # (B)(construct selector from response)
        for selector in scrapy.selector.Selector(response=response).xpath('//ol[@class="grid_view"]/li/div[@class="item"]'):
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
            # print 'rank', rank
            # print 'pic', pic
            # print 'title', title
            # print 'url', url
            # print 'desc', desc
            # print 'star', star
            # print 'rate', rate
            # print 'comment', comment
            # print 'quote', quote
            yield item
        # [2][extract links from the page, follow them, and then extract data from the pages]
        next_page = response.xpath('//span[@class="next"]/a/@href').extract()  # [u'?start=200&filter=']
        if next_page:
            next_url = response.urljoin(next_page[0])  # http://movie.douban.com/top250?start=25&filter=
            yield scrapy.Request(next_url, self.parse_item)
