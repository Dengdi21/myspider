"""
爬取斗鱼直播

思路：
1.利用selenium得到页面内容
2.利用xpath或者bs4等在页面中获取信息
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import os


class Douyu():
    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'

    def setUP(self):
        chromedriver = '/Users/chunmu/Desktop/chromedriver'
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

    def douyu(self):
        self.driver.get(self.url)


        while True:
            soup = BeautifulSoup(self.driver.page_source, 'xml')

            # 返回页面信息（标题列表和观众人数）
            titles = soup.find_all('h3', {'class': 'ellipsis'})
            nums = soup.find_all('span', {'class': 'dy-num fr'})

            for title, num in zip(titles, nums):
                print("房间：{0}，总共观赏人数：{1}".format(title.get_text().strip(), num.get_text().strip()))

    def sestr(self):
        self.driver.quit()


if __name__ == '__main__':
    douban = Douyu()

    douban.setUP()
    douban.douyu()
    douban.sestr()
