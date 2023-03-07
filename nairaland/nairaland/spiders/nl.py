import scrapy
from ..items import NairalandItem
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class NlSpider(CrawlSpider):
    name = 'nl'
    allowed_domains = ['nairaland.com']
    start_urls = ['https://www.nairaland.com/news/5200']


    rules = (
        Rule(
            LinkExtractor(restrict_xpaths=('//table[@summary="links"]')),
            callback="parse",
            follow=True),

        Rule(
            LinkExtractor(restrict_xpaths=('//div[@class ="body"]/p[3]')),
            callback="parse", follow=True),)

    def parse(self, response):
        item = ItemLoader(item=NairalandItem(), response=response, selector=response)
        item.add_xpath('poster', '//table[@summary="posts"]//tr[1]//td/a[@class="user"]/text()')
        item.add_xpath('time', '//table[@summary="posts"]//tr[1]//td/span[@class="s"]/b[1]/text()')
        item.add_xpath('views', '//p[@class="bold"]/text()')
        item.add_xpath('news_category', '//p[@class="bold"]/a[3]/text()')
        item.add_xpath('news', '//p[@class="bold"]/a[4]/text()')
        item.add_xpath('date', '//table[@summary="posts"]//tr[1]//td/span[@class="s"]/b[2]/text()')
        item.add_xpath('date', '//table[@summary="posts"]//tr[1]//td/span[@class="s"]/b[3]/text()')
        item.add_value('url', response.url)
        yield item.load_item()
