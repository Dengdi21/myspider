"""

https://www.ximalaya.com/yinyue/minyao/

汉字转换为拼音

"""
import json
from urllib import request

from pypinyin import pinyin
from pypinyin import lazy_pinyin

# 包的简单用法
a = "图灵"
print(pinyin(a))
print(lazy_pinyin(a))
print(''.join(lazy_pinyin(a)))

# 喜马拉雅音乐下载
import requests
from selenium import webdriver
import os
import time
import re

chromedriver = '/Users/chumu/Desktop/chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

def fanyi(num):
    """
    翻译要查找的类型为拼音
    :param num:
    :return:
    """
    var = lazy_pinyin(num)
    str = ''.join(var)
    return str


# 获取详情页
def start_spider(str, headers):
    url = "https://www.ximalaya.com/yinyue/{}/".format(str)
    print(url)

    driver.get(url)
    html = driver.page_source
    # print(html)

    return html


# 获取albumID值
def get_albumID(html, headers):
    albumID = re.findall(r'"albumId":(.*?),', html)
    print(albumID)

    albumID = albumID[7:8][0]
    # 构建下载地址
    down_url = "https://www.ximalaya.com/revision/play/v1/show?id={}&sort=1&size=30&ptype=1".format(albumID)
    print(down_url)

    # 请求音乐json文件
    driver.get(down_url)
    html = driver.page_source
    print(html)
    return html


def download_music(music_json):
    music_json = json.loads(music_json)

    # 获取标题和下载链接
    titles = music_json['data']['tracksAudioPlay']
    for title in titles:
        print(title['trackName'])
        print(title['src'])

        # 下载
        request.urlretrieve(title['src'], './music' + title['trackName'])


if __name__ == '__main__':
    music_type = input("plese input your music type:")

    music_type = fanyi(music_type)

    headers = {
        'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0'
    }

    html = start_spider(music_type, headers)
    music_json = get_albumID(html, headers)
    download_music(music_json)



