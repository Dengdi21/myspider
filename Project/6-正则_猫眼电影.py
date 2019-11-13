"""
利用正则来爬取猫眼电影
1.猫眼电影榜单url：https://maoyan.com/board
2.把电影信息尽可能多的获取

注：猫眼有了反爬措施，数据已经加密，这里使用模拟浏览器的方法获取加密数据

分析:
1.一个影片的内容在标签<dd></dd>中
2.在单元内存在一部电影的所有信息

思路：
1.利用re把dd中的信息提取出来
2.利用re在每个dd标签中提取单部电影的信息
"""

"""
步骤：
1.获取榜单源代码
2.提取所有dd标签
3.获取单部电影信息
"""
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from urllib import request, parse
import requests

# 1.下载榜单页面源码

url = "https://maoyan.com/board"

# 模拟浏览器拿到源代码
from selenium import webdriver
import os

chromedriver = '/Users/chunmu/Desktop/chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver
# option = webdriver.ChromeOptions()
# option.add_argument('--headless')
# driver = webdriver.Chrome(chromedriver, chrome_options=option)
driver = webdriver.Chrome(chromedriver)
driver.get(url)
# 网页源码
html = driver.page_source
# print(html)
# 关闭浏览器
driver.close()

# 2.提取网页信息
import re

s = r'<dd>(.*?)</dd>'
"""
如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始，不会跨行。
而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，将“\n”当做一个普通的字符加入到这个字符串中，
在整体中进行匹配。
"""
pattern = re.compile(s, re.S)
movies = pattern.findall(html)
print(len(movies))

# 3.从每个匹配到的结果中获取每部电影的信息
for movie in movies:
    # 提取电影名称
    s = r'<a.*?title="(.*?)"'
    pattern = re.compile(s)
    title = pattern.findall(movie)[0]
    print(title)










