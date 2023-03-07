import scrapy
from ..items import FreeimagesItem
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ImagesSpider(CrawlSpider):
    name = 'images'
    allowed_domains = ['freeimages.com']
    start_urls = ['http://freeimages.com/']

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths=('//div[contains(@class, "masonry-container")]')),
            callback="parse",
            follow=False),)

    def parse(self, response):
        item = ItemLoader(item=FreeimagesItem(), response=response, selector=response)
        item.add_css('image_urls', 'img#photo::attr("src")')
        #item.add_xpath('images', '//div[contains(@class, "ImageCard-module")]//img')
        yield item.load_item()


