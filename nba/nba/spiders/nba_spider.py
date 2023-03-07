import scrapy
from scrapy.loader import ItemLoader
from selenium import webdriver
from selenium.webdriver.common.by import By
from ..items import NbaItem
import time
# Building of scrapy framework for parsing the website
class NbaspiderSpider(scrapy.Spider):
    name = 'nbaspider'

    # Integration of Selenium into Scrapy

    def start_requests(self):
        driver = webdriver.Chrome(executable_path='C:\drivers\chromedriver.exe')
        driver.get('https://www.nba.com/stats/alltime-leaders?')
        driver.maximize_window()
        time.sleep(3)

        cookie = driver.find_element(By.CSS_SELECTOR, value='button#onetrust-accept-btn-handler')
        cookie.click()
        time.sleep(3)
        #pagination
        pagination = driver.find_element(By.XPATH, value='//div[contains(@class, "Pagination_content")]')
        pages = pagination.find_elements(By.XPATH, value='.//select[option="All"]//option')
        last_page = int(pages[-1].text)
        current_page = 1
        while current_page <= last_page:
            for link in driver.find_elements(By.XPATH, value=('//td[@class="Crom_text__NpR1_ Crom_primary__EajZu Crom_stickySecondColumn__29Dwf"]//a')):
                players_link = link.get_attribute('href')
                yield scrapy.Request(players_link)

            current_page=+1
            try:
                next_button = driver.find_element(By.XPATH,value='//button[@title="Next Page Button"]')
                next_button.click()
            except:
                break
        driver.quit()
    # Parsing of the website
    def parse(self, response):
        item = ItemLoader(item=NbaItem(), response=response, selector=response)
        item.add_xpath('player_info', '//p[@class="PlayerSummary_mainInnerInfo__jv3LO"]/text()')
        item.add_xpath('player_name', '//p[contains(@class, "playerNameText")][1]/text()')
        item.add_xpath('player_name', '//p[contains(@class, "playerNameText")][2]/text()')
        item.add_xpath('player_height', '//div[p="HEIGHT"]/p[@class="PlayerSummary_playerInfoValue__JS8_v"]/text()')
        item.add_xpath('player_weight', '//div[p="WEIGHT"]/p[@class="PlayerSummary_playerInfoValue__JS8_v"]/text()')
        item.add_xpath('player_nationality', '//div[p="COUNTRY"]/p[@class="PlayerSummary_playerInfoValue__JS8_v"]/text()')
        item.add_xpath('last_attended', '//div[p="LAST ATTENDED"]/p[@class="PlayerSummary_playerInfoValue__JS8_v"]/text()')
        item.add_xpath('player_age', '//div[p="AGE"]/p[@class="PlayerSummary_playerInfoValue__JS8_v"]/text()')
        item.add_xpath('player_birthdate', '//div[p="BIRTHDATE"]/p[@class="PlayerSummary_playerInfoValue__JS8_v"]/text()')
        item.add_xpath('nba_draft', '//div[p="DRAFT"]/p[@class="PlayerSummary_playerInfoValue__JS8_v"]/text()')
        item.add_xpath('years_of_experience', '//div[p="EXPERIENCE"]/p[@class="PlayerSummary_playerInfoValue__JS8_v"]/text()')
        item.add_xpath('player_points_per_game', '//div[p="PPG"]//p[@class="PlayerSummary_playerStatValue___EDg_"]/text()')
        item.add_xpath('player_rebounds_per_game', '//div[p="RPG"]//p[@class="PlayerSummary_playerStatValue___EDg_"]/text()')
        item.add_xpath('player_assists_per_game', '//div[p="APG"]//p[@class="PlayerSummary_playerStatValue___EDg_"]/text()')
        item.add_xpath('player_pie', '//div[p="PIE"]//p[@class="PlayerSummary_playerStatValue___EDg_"]/text()')
        yield item.load_item()
