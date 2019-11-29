# -*- coding: utf-8 -*-
import scrapy
from ..items import MYNum5QidianItem


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/free']

    def parse(self, response):
        infos = response.xpath('//div[@class="book-img-text"]/ul/li')
        # print(infos)
        for info in infos:
            print(info)
            title = info.xpath('.//div[@class="book-mid-info"]/h4/a/text()').extract()[0]
            href = info.xpath('.//div[@class="book-mid-info"]/h4/a/@href').extract()[0]
            href = 'https:' + href

            print(title)
            print(href)
            item = MYNum5QidianItem()
            item['title'] = title
            item['href'] = href

            yield item
            yield scrapy.Request(url=href, callback=self.parse_detail, meta={'data': item, 'phantomjs': True}, dont_filter=True)
            # 添加参数phantomjs为True，在自定义中间件中进行判断，为True的才走自定义中间件


    def parse_detail(self, response):
        """
        详情页
        :param response:
        :return:
        """
        print('1111')
        item = response.meta['data']

        # 作者
        author = response.xpath('//div[@class="book-info"]//span/a/text()').extract()[0]
        info = response.xpath('//p[@class = "intro"]/text()').extract()[0]

        item['author'] = author
        item['info'] = info

        yield item




