# Importing of the necessary libraries
from ..items import NairalandItem
from scrapy.loader import ItemLoader
import scrapy
from scrapy import Request


# Building of scrapy framework for parsing the website

class TotalspiderSpider(scrapy.Spider):
    name = 'nl'
    current_page = 2
    start_urls = ['https://www.nairaland.com/news/']


# Extracting links from all the pages


    def parse(self, response):
        links =  response.css('[summary="links"] a::attr(href)').getall()
        for link in links:
            yield Request(url=link, callback=self.parse_categories)
        total_pages = int(response.css('div.body p:nth-child(6) b:last-child::text').get())
        url = 'https://www.nairaland.com/news/' + str(TotalspiderSpider.current_page)
        if TotalspiderSpider.current_page <= total_pages:
            TotalspiderSpider.current_page += 1
            yield Request (url=url, callback=self.parse)


# Parsing of the website

    def parse_categories(self, response):
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


