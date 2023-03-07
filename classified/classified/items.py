# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, Join

def clean(s):
    return s[0].replace('\t', "").replace('\n', "").replace(u'\xa0', u" ").strip("\t")


class ClassifiedItem(scrapy.Item):
    title = scrapy.Field(output_processor=clean)
    locality = scrapy.Field(output_processor=clean)
    address = scrapy.Field(output_processor=clean)
    description = scrapy.Field(output_processor=clean)
    landline = scrapy.Field(output_processor=clean)
    mobile = scrapy.Field(output_processor=clean)
    price = scrapy.Field(output_processor=clean)