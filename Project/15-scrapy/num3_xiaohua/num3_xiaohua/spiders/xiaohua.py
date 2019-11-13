# -*- coding: utf-8 -*-
import scrapy

from urllib import request
from ..items import XiaoHuaItem


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['521609.com']
    start_urls = ['http://521609.com/']

    def parse(self, response):

        bookmarks = request.xpath('//ul/li')

        for bm in bookmarks:
            item = XiaoHuaItem()

            item['title']= bm.xpath('./a/img/@alt').eextract()[0]
            item['href']= bm.xpath('./a/img/@src').eextract()[0]

            yield item
