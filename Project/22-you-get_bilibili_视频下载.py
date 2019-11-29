"""
先自行安装you-get

1.打开哔哩哔哩网站，搜索"视频"
2.在网页中查找到存放搜索到的视频的信息，存放在json文件中；
不能只单在前两页找，找到第三页时发现网址：
https://api.bilibili.com/x/web-interface/search/type?context=&page=6&order=&keyword=%E8%A7%86%E9%A2%91&duration=&tids_1=&tids_2=&__refresh__=true&search_type=video&highlight=1&single_column=0&jsonp=jsonp
4.分析视频播放地址
https://www.bilibili.com/video/av76580025
编号可在2中网址的json文档中获取。
"""

import json
import os
import requests

def getInfo(start_page, endpage):
    """
    获取srcurl地址和title
    :param start_page:
    :param endpage:
    :return:
    """
    data = []
    for page in range(start_page, endpage + 1):
        url = 'https://api.bilibili.com/x/web-interface/search/type?context=&page={}' \
              '&order=&keyword=%E8%A7%86%E9%A2%91&duration=&tids_1=&tids_2=&__' \
              'refresh__=true&search_type=video&highlight=1&single_column=0&jsonp=jsonp'.format(page)

    decode = requests.get(url).text
    decodejson = json.loads(decode)
    # print(decodejson)

    items = decodejson['result']
    for item in items:
        title = item['title']
        video_url = item['arcur']
        data.append([title, video_url])

    return data

def downloadvide(data):
    path = './nusic'
    if not os.path.exists(path):
        os.makedirs(path)

    for title, url in data:
        # 存储路径
        root = path + "\\" + title

        print('--------------------------')
        print('正在下载视频：{}......'.format(title))
        # 使用os.system操作you-get进行视频下载
        os.system("you-get -u {} {}".format(root, title))
        print('视频下载完成：{}......'.format(title))


if __name__ == '__main__':
    data = getInfo(1, 2)
    downloadvide(data)