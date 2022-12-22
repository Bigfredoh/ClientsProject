import scrapy


class NachiSpiderSpider(scrapy.Spider):
    name = 'nachi_spider'
    allowed_domains = ['x']
    start_urls = ['http://x/']

    def parse(self, response):
        pass
