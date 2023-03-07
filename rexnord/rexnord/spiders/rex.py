import scrapy


class RexSpider(scrapy.Spider):
    name = 'rex'
    allowed_domains = ['rexnord.com']
    start_urls = ['http://rexnord.com/']

    def parse(self, response):
        pass
