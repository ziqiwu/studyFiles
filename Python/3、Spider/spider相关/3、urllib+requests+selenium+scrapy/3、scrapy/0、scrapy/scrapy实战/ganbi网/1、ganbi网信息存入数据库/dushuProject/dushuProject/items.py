# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DushuprojectItem(scrapy.Item):
    title = scrapy.Field()
    pub_time = scrapy.Field()
    see = scrapy.Field()
    info_url = scrapy.Field()
    duration = scrapy.Field()


class DushuItem(scrapy.Item):
    title = scrapy.Field()
    pub_time = scrapy.Field()
    see = scrapy.Field()
    info_url = scrapy.Field()
    duration = scrapy.Field()