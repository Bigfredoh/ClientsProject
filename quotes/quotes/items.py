# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Join
def clean(s):
    return s[0].replace('\u201c', '').replace('\u201d', '').replace('\u00e9', '')


class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    quote = scrapy.Field(input_processor = clean, output_processor = Join())
    author= scrapy.Field(input_processor = clean, output_processor = Join())
    tags= scrapy.Field(output_processor = Join())

