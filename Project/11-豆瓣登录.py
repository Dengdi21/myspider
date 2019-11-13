"""
利用selenium模拟登录豆瓣
需要输入验证码：
    思路:
        1.保存页面或快照
        2.等待用户手动输入验证码
        3.继续自动执行提交动作
"""

from selenium import webdriver
# 键盘输入
from selenium.webdriver.common.keys import Keys
import time
import os

url = 'https://accounts.douban.com/passport/login'
chromedriver = '/Users/chunmu/Desktop/chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get(url)

time.sleep(4)

# 生成快照用来查看验证码
driver.save_screenshot('douban_index.png')

captcha = input("pleses input your code:")

# 利用账号信息进行登录
driver.find_element_by_id("email").send_keys("15284691807")
driver.find_element_by_id("password").send_keys("sdkjhfhg")
driver.find_element_by_id("captcha_field").send_keys(captcha)

driver.find_element_by_name("user_login").click()

time.sleep(5)

driver.save_screenshot("logined.png")

with open("douban_home.html", 'w', encoding='utf-8') as f:
    f.write(driver.page_source)

driver.quit()


