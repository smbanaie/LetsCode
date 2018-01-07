# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BanaieCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    body = scrapy.Field()
    category = scrapy.Field()
    section = scrapy.Field()
    tags = scrapy.Field()
    pubDate = scrapy.Field()
