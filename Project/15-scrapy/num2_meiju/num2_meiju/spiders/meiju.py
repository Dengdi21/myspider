# -*- coding: utf-8 -*-
import scrapy

from ..items import MeiJuItem


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijuxz.com']
    start_urls = ['http://meijuxz.com/']

    def parse(self, response):
        """
        默认已经得到了网页
        反馈的内容用response表示
        其中包含了需要的所有数据
        :param response:
        :return:
        """
        # 找到所有的最新电影
        movies = response.xpath('//ul[@class="stui-vodlist clearfix"]/li')
        print(movies)
        for movie in movies:
            '''
            每个movie都需要转换成一个item
            '''

            item = MeiJuItem()
            item['name'] = movie.xpath('./div/a/@title').extract()[0]
            item['href'] = movie.xpath('./div/a/@href').extract()[0]
            item['tv'] = 'meiju'
            item['state'] = movie.xpath('./div/div/h4/a/text()').extract()[0]

            # item只通过yield返回
            yield item