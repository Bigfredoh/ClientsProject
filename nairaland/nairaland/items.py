# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy
from itemloaders.processors import MapCompose, Join
import re

from twisted.web.client import _urljoin


def clean(s):
    return re.sub(r"\D", "", str(s))



class NairalandItem(scrapy.Item):
    # define the fields for your item here like:
    news = scrapy.Field(output_processor=Join())
    news_category = scrapy.Field(output_processor=Join())
    poster = scrapy.Field(output_processor=Join())
    time = scrapy.Field(output_processor=Join())
    date = scrapy.Field(output_processor=Join())
    views = scrapy.Field(output_processor=clean)
    url = scrapy.Field(output_processor=Join())


