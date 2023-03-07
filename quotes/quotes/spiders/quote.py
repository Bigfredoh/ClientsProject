import scrapy
from scrapy_splash import SplashRequest
from ..items import QuotesItem
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class QuoteSpider(CrawlSpider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    lua_script = """"
        function main(splash)
            local num_scrolls = 20
            local scroll_delay = 1
        
            local scroll_to = splash:jsfunc("window.scrollTo")
            local get_body_height = splash:jsfunc(
                    "function() {return document.body.scrollheight;}"
            )
            assert(splash:go(splash.args.url))
            splash:wait(splash.args.wait)
        
            for _ = 1, num_scrolls do
                local height = get_body_height()
                for i =1, 10 do
                    scroll_to(0,height*i/10)
                    splash:wait(scroll_delay/10)
                end
            end
            return splash:html()
        end
    """

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url = url, endpoint="execute", callback=self.parse, args={
                'wait':1,
                "lua_source": self.lua_script
            })

    def parse(self, response):
        container = response.xpath('//div[@class="quote"]')
        for q in container:
            item = ItemLoader(item=QuotesItem(), response=response, selector=q)
            item.add_xpath('quote', './/span[@class="text"]/text()')
            item.add_xpath('author', './/span//small[@itemprop="author"]/text()')
            item.add_xpath('tags', './/div[@class="tags"]/a/text()')
            yield item.load_item()
