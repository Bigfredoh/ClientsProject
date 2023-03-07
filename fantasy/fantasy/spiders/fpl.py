import scrapy
from scrapy_splash import SplashRequest
from ..items import FantasyItem
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class FplSpider(CrawlSpider):
    name = 'fpl'
    allowed_domains = ['premierleague.com']
    start_urls = ['https://www.premierleague.com/stats/top/players/goals?se=-1&cl=-1&iso=-1&po=-1?se=-1']

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths=('//div[@class="sidebarPush"]')),
            callback="parse",
            follow=True),

        Rule(
            LinkExtractor(restrict_text=('Next')),
            callback="parse", follow=True),)

    def parse(self, response):
        item = ItemLoader(item=FantasyItem(), response=response, selector=response)
        item.add_xpath('nationality', '//li[div = "Nationality"]/div[@class ="info"]/span[@ class ="playerCountry"]/text()')
        item.add_xpath('name', '//div[@class="playerDetails"]/h1/div/text()')
        item.add_xpath('height', '//li[div = "Height"]//div[@class="info"]/text()')
        item.add_xpath('DOB', '//li[div = "Date of Birth"]//div[@class="info"]/text()')
        item.add_xpath('golden_boot', '//tr[th="Golden Boot"]//th[@class="u-text-right"]/text()')
        item.add_xpath('player_of_the_season', '//tr[th="Player of the Season"]//th[@class ="u-text-right"]/text()')
        item.add_xpath('goal_of_month', '//tr[th="Goal of the Month"]//th[@class="u-text-right"]/text()')
        item.add_xpath('premier_league_champion', '//tr[th="Premier League Champion"]//th[@class="u-text-right"]/text()')
        item.add_xpath('player_of_the_month', '//tr[th = "Player of the Month"]//th[@class ="u-text-right"]/text()')
        item.add_xpath('player_of_the_month', '//tr[th = "Player of the Month"]//th[@class ="u-text-right"]/text()')
        item.add_xpath('position', '//nav[@class="fixedSidebar"]//section/div[@class="info"]/text()')
        yield item.load_item()




