import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TourriderSpider(CrawlSpider):
    name = 'tourrider'
    allowed_domains = ['subscriber.tourready.com']
    start_urls = ['https://subscriber.tourready.com/vendor/searchvendor']

    rules = (
        Rule(LinkExtractor(restrict_css='a.viewCompProfileBtn'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        pass
