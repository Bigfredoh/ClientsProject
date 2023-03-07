# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, Join
def extract(s):
    return s[0]


class PhoneModelsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(output_processor=extract)
    announced= scrapy.Field( output_processor=Join())

