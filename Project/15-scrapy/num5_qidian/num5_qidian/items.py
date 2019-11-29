# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Num5QidianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MYNum5QidianItem(scrapy.Item):
    # 首页内容
    title = scrapy.Field()
    href = scrapy.Field()

    # 详情页内容
    author = scrapy.Field()
    info= scrapy.Field()
