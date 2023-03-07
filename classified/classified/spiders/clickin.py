import scrapy
from ..items import ClassifiedItem
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ClickinSpider(CrawlSpider):
    name = 'clickin'
    #allowed_domains = ['clickin.com']
    start_urls = ['https://www.click.in/automobiles-ctgid150']

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths=('//div[@id="classifieds_list"]')),
            callback="parse",
            follow=True),)

    def parse(self, response):
        item = ItemLoader(item=ClassifiedItem(), response=response, selector=response)
        item.add_xpath("title", '//div[@class = "clickin-post-details clearfix"]/h1/text()')
        item.add_xpath("address", '//div[div = "Address"]/div/p/text()')
        item.add_xpath("locality", '//td/div[@class="clickin-post-blackbold"]/text()')
        item.add_xpath("description", '//div[@class="clickin-description"]/p[@class="clickin-desc-text"]/text()')
        item.add_xpath("landline", '//div[div = "Landline"]/div[@class="clickin-post-blackbold"]/text()')
        item.add_xpath("mobile", '//div[div = "Mobile"]/div[@class="clickin-post-blackbold"]/text()')
        item.add_xpath("price", '//td[div="Price"]/div[@class="clickin-post-blackbold"]/text()')
        yield item.load_item()
