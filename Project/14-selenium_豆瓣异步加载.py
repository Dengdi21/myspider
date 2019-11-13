"""
任务
1.利用selenium模拟鼠标下拉
2.每次多出现几部电影
"""

from selenium import webdriver
import os
import time

chromedriver = '/Users/chunmu/Desktop/chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
driver.get(url)

# 向下滚动10000像素
js = 'document.body.scrollTop=10000'

# 滚动前
time.sleep(3)
driver.save_screenshot('doubaimovie.png')

# 滚动后
driver.execute_script(js)
driver.save_screenshot('doubaimovie2.png')
time.sleep(3)