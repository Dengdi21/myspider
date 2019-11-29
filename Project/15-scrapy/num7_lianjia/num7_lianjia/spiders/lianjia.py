# -*- coding: utf-8 -*-
import os
import random
import time

import scrapy

from ..settings import headers
from ..items import MYLianjiaItem
from urllib import request


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    # start_urls = ['http://lianjia.com/']

    def start_requests(self):
        """
        定义抓取地址
        :return:
        """
        start_urls =[]
        for page in range(2, 3):
            urls = 'https://cd.lianjia.com/zufang/jinjiang/pg{}rp2'.format(page)
            start_urls.append(urls)

        print(headers)
        for start_url in start_urls:
            yield scrapy.Request(url=start_url, callback=self.parse, dont_filter=True, headers=headers)

    def parse(self, response):
        # print(response.body.decode('utf-8'))
        # 每页全部房源信息列表
        infos = response.xpath('//div[@class="content__list"]/div[@class="content__list--item"]')
        print(infos)

        for info in infos:
            # 获取标题
            house_title = info.xpath('.//p[@class="content__list--item--title twoline"]/a/text()').extract()
            house_title =house_title[0].strip().replace(' ', '')
            # print(house_title)

            # 详情链接
            house_href = info.xpath('.//p[@class="content__list--item--title twoline"]/a/@href').extract()
            house_href = "https://cd.lianjia.com" + house_href[0]
            # print(house_href)

            # 获取小区名称
            house_name = info.xpath('.//p[@class="content__list--item--des"]//a/text()').extract()
            house_name = '-'.join(house_name)
            # print(house_name)

            data = {
                "house_title": house_title,
                "house_href": house_href,
                "house_name": house_name
            }
            time.sleep(random.choice([0.3, 0.5, 0.4, 3, 2, 1, 0.6]))
            yield scrapy.Request(url=house_href, callback=self.detail_parse, dont_filter=True, headers=headers, meta=data)

    def detail_parse(self, response):
        """
        获取房屋详情页
        :param response:
        :return:
        """
        infos = response.xpath('//div[@class="content clear w1150"]')

        for info in infos:
            # 房源编号
            house_num = info.xpath('.//i[@class="house_code"]/text()').extract()
            house_num = house_num[0].split('：')[-1]
            # print(house_num)

            # 房屋价格
            house_price = info.xpath('.//div[@class="content__aside--title"]/span/text()').extract()
            house_price = house_price[0] + '元/月'
            # print(house_price)

            # # 经纪人
            # house_people = info.xpath('.//span[@class="contact__name"]/@title').extract()
            # print(house_people)

            # 租赁方式
            house_way = '未知'

            # 厅室
            house_ting = '略'
            # 大小
            house_size = '略'
            # 方向
            house_toward = '略'

            # 图片地址
            house_imgs = 'lianjia/{}'.format(response.meta["house_title"])

            item = MYLianjiaItem()

            item['house_title'] = response.meta["house_title"]
            item['house_href'] = response.meta["house_href"]
            item['house_name'] = response.meta["house_name"]
            item['house_num'] = house_num
            item['house_price'] = house_price
            item['house_style'] = house_way
            item['house_ting'] = house_ting
            item['house_size'] = house_size
            item['house_toword'] = house_toward
            item['house_imagdir'] = house_imgs

            print(item)

            yield item

            # 图片下载处理
            # house_img_urls = info.xpath('.//div[@class="content__article__slide__item"]/img/@src').extract()
            # if len(house_img_urls) != 0:
            #     for house_img_url in house_img_urls:
            #         img_name = str(time.time()) + '.jpg'
            #         if not os.path.exists(house_imgs):
            #             os.mkdir(house_imgs)
            #
            #         request.urlretrieve(house_img_url,house_imgs + '/' + img_name)
