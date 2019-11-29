import time

from selenium import webdriver
from scrapy.http.response.html import HtmlResponse


class QIDIANDownloaderMiddleware(object):
    def __init__(self):
        print('初始化自定义中间件')
        self.driver = webdriver.PhantomJS()

    def process_request(self, request, spider):
        """

        :param request:
        :param spider:
        :return:
        """
        # 只处理详情页
        if request.mete.get('phantomjs', True):
            print('走自定义中间件了')
            self.driver.get(request.url)
            time.sleep(1)
            html = self.driver.page_source

            return HtmlResponse(url=request.url, body=html, encoding='utf-8',request=request)