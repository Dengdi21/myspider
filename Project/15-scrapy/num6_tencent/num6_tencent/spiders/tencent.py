# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://tencent.com/']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )
    # 每一页链接
    page_list = LinkExtractor(allow=('start=\d+'))

    rules = (
        Rule(LinkExtractor(page_list), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        enen_l = response.xpath('//tr[@class="enen"]')
        odd_l = response.xpath('//tr[@class="odd"]')
        res_list = enen_l + odd_l
        print(res_list)

        for res in res_list:
            title = res.xpath('./td[1]/a/text()').extract()[0]
            info = res.xpath('./td[1]/a/@href').extract()[0]
            postion_info = res.xpath('./td[2]/text()').extract()[0]
