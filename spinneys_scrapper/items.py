# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpinneysscraperItem(scrapy.Item):
    img = scrapy.Field()
    name = scrapy.Field()
    price_before = scrapy.Field()
    price_after = scrapy.Field()
    category = scrapy.Field()