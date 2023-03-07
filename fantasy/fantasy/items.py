# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import re
import scrapy
from itemloaders.processors import Join, TakeFirst

def clean(s):
    return re.sub(r"[\\n\s]", "", str(s))


class FantasyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor =clean, output_processor = Join())
    nationality = scrapy.Field(output_processor = Join())
    height = scrapy.Field(output_processor = Join())
    DOB = scrapy.Field(input_processor =clean, output_processor = TakeFirst())
    golden_boot= scrapy.Field(output_processor = TakeFirst())
    player_of_the_season = scrapy.Field(output_processor = TakeFirst())
    goal_of_month = scrapy.Field(output_processor = TakeFirst())
    premier_league_champion =  scrapy.Field(output_processor = TakeFirst())
    player_of_the_month = scrapy.Field(output_processor = TakeFirst())
    position = scrapy.Field(input_processor =clean, output_processor = TakeFirst())