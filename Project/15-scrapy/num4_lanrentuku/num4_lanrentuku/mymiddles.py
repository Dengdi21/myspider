import time

from selenium import webdriver

from fake_useragent import UserAgent

import random
class LrtkDownloaderMiddleware(object):
    def __init__(self):
        self.ug = UserAgent()

    def process_request(self, request, spider):
        """
        
        :param request: 请求对象
        :param spider: 爬虫对象
        :return: 
        """
        # 加入头部
        request.headers.setdefalult('user-agent', self.ug.random)

        # 构建浏览器
        driver = webdriver.Chrome()
        driver.get(request.url)
        time.sleep(1)
        driver.save_screenshot('1.png')

        """
        略
        """