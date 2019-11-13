"""
任务：
通过selenium模拟对页面的控制
"""

from selenium import webdriver
import os
import time

chromedriver = '/Users/chunmu/Desktop/chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

url = 'https://www.baidu.com/'
driver.get(url)

# 通过js来控制网页内容
# 需要先把js编写出来
# 通过execute_script执行

"""
美化输入框，输入框id是kw
"""

js = "var q=document.getElementById(\'kw\'); q.style.border=\'2px_solid_red\';"

# 执行代码
driver.execute_script(js)

time.sleep(3)
driver.save_screenshot('readbaidu.png')

# js隐藏相应元素，这里隐藏logo
img = driver.find_element_by_xpath('//*[@id="lg"]/img')

driver.execute_script('$(arguments[0]).faderOut()', img)

# 滚动滑动条到最底下
js = "$('.scroll_top').click(function(){$('html, body).animate({scrollTop: '0px}, 800)});"

# 查看网页快照
driver.save_screenshot("nullbaidu.png")

