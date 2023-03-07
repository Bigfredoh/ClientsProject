import scrapy
from ..items import PhoneModelsItem
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class GsmarenaSpider(CrawlSpider):
    name = 'gsmarena'
    allowed_domains = ['gsmarena.com']
    start_urls = ['https://www.gsmarena.com/makers.php3']

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths=('//div[@class="st-text"]')),
            callback="parse", follow=True),
        Rule(
            LinkExtractor(restrict_xpaths=('//div[@class="makers"]')),
            callback="parse", follow=True),)

    def parse(self, response):
        item = ItemLoader(item=PhoneModelsItem(), response=response, selector=response)
        item.add_xpath('title', '//h1[@class="specs-phone-name-title"]/text()')
        item.add_xpath('announced', '//table//tr/td[@data-spec="status"]/text()')
        yield item.load_item()
