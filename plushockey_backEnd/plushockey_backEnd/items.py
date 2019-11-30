# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Match(Item):
    home_team = Field()
    away_team = Field()
    score_home = Field()
    score_away = Field()
    date_time = Field()
    # league = Field()
    

