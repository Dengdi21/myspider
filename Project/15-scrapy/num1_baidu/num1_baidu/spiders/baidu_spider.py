"""
导入scrapy
所有类一般是xxxspider的子类

"""

import scrapy


class BaiduSpider(scrapy.Spider):
    # name是爬虫的名称
    name = "baidu"

    # 起始url列表
    start_urls = ['http://www.baidu.com']

    # 负责分析downloader下载得到的结果
    def parse(self, response):
        """
        只是得到网页即可
        :param response:
        :return:
        """
        with open('baidu1.html', 'w', encoding='utf-8') as f:
            f.write(response.body.decode('utf-8'))

        with open('baidu2.html', 'w', encoding='utf-8') as f:

            s = 'dkjhgkjdsgd'
            f.write(s)
