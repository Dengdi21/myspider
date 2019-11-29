# -*- coding: utf-8 -*-
import os
import re

import scrapy
from urllib import request


class LanrentukuSpider(scrapy.Spider):
    name = 'lanrentuku'
    allowed_domains = ['lanrentuku.com']
    start_urls = []
    base_urls = ['http://www.lanrentuku.com/vector/flower/p{}.html']

    for page in range(1, 2):
        start_urls.append(base_urls[0].format(page))

    print(start_urls)

    root_dir = 'picture'

    if not os.path.exists(root_dir):
        os.mkdir(root_dir)

    def parse(self, response):
        # print(response.text)
        paths = response.url.split('/')
        with open(paths[-1], 'w', encoding='utf-8') as f:
            f.write(response.body.decode('GBK'))

        dd_list = response.xpath('//div[@class="list-pic"]/dl/dd')
        for dd in dd_list:
            print(type(dd))

            # 匹配缩略图
            # pattern = re.compile(r'<img.*src="(.*?)">')
            # src = pattern.findall(dd)
            # print(src)

            # 详情页
            pattern = re.compile(r'<a.*href="(.*?)"')
            a_list = pattern.findall(dd)
            if a_list is not None:
                href = a_list[0]
                href = request.urljoin(response.url, href)
                print(href)

                yield scrapy.Request(url=href, callback=self.detail_page)

    def detail_page(self, response):
        """
        解析详情页
        :param response:
        :return:
        """
        imgs = response.xpath('//div[@class="content-a"]/p/img/@src').extract()
        print(imgs)
        yield scrapy.Request(url=imgs, callback=self.download_pic)

    def download_pic(self, response):
        path = response.url.split('/')
        filename = self.root_dir + '/' + path[-1]

        with open(filename, 'wb') as f:
            f.write(response.body)


