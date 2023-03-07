# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Join, TakeFirst
import re





class NbaItem(scrapy.Item):
    # define the fields for your item here like:
    player_info= scrapy.Field(output_processor = Join())
    player_name = scrapy.Field(output_processor = Join())
    player_height = scrapy.Field( output_processor = Join())
    player_weight = scrapy.Field( output_processor = Join())
    player_nationality = scrapy.Field(output_processor = TakeFirst())
    last_attended= scrapy.Field(output_processor = TakeFirst())
    player_age = scrapy.Field(output_processor = Join())
    player_birthdate = scrapy.Field(output_processor = TakeFirst())
    nba_draft = scrapy.Field(output_processor = TakeFirst())
    years_of_experience = scrapy.Field(output_processor = TakeFirst())
    player_points_per_game = scrapy.Field(output_processor = Join())
    player_rebounds_per_game = scrapy.Field(output_processor = Join())
    player_assists_per_game = scrapy.Field(output_processor = Join())
    player_pie = scrapy.Field(output_processor = Join())

