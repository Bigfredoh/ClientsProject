from scrapy_selenium import SeleniumRequest
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from scrapy.loader import ItemLoader
from ..items import NbaStatItem



class NbaSpider(scrapy.Spider):
    name = 'nba'

    def start_requests(self):
        url = 'https://www.nba.com/stats/alltime-leaders?ActiveFlag=No'
        yield SeleniumRequest(url=url, callback=self.parse)


    def parse(self, response):
        container = response.xpath('//tbody[@class="Crom_body__UYOcU"]//tr')
        for stats in container:
            item = ItemLoader(item=NbaStatItem(), response=response, selector=stats)
            item.add_xpath('player_name', './/td[@class="Crom_text__NpR1_ Crom_primary__EajZu Crom_stickySecondColumn__29Dwf"]//a/text()')
            yield item.load_item()