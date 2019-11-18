# open(fileName, 'wb') as f:
#     while f:


"""
二进制文件的存储（音频，视频......）
1. 获取到下载文件的url  二进制方式下载
2.使用urllib模块的urlretrieve()可以进行音频文件下载
    也支持远程下载到本地

urlretrieve(url, filename=None, reporthook=None, data=None)
url: 文件地址
filename： 存储路径/文件名
reporthook： 回调函数，连接上服务器时或相应数据下载完成后触发该函数
            一般用来显示当前下载进度
data： （filename， headers）元祖

"""

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from urllib import request

import requests
import os
from lxml import etree

headers = {
    "User-Agent": "Mozilla / 5.0(Macintosh;IntelMacOSX10_14_2) AppleWebKit / \
    537.36(KHTML, likeGecko) Chrome / 78.0.3904.87Safari / 537.36"}

url = 'https://www.ivsky.com/tupian/ziranfengguang/'


# 回调函数
def Schedule(blocknum, blocksize, totalsize):
    """
    显示下载进度
    :param blocknum: 已下载数据块
    :param blocksizi: 数据块大小
    :param totalsize: 文件大小
    :return: None
    """
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
    print('当前下载进度: {}'.format(per))



rsp = requests.get(url, headers=headers)

# print(rsp.text)

html = etree.HTML(rsp.text)

# 找到所有图片连接
img_url = html.xpath('//div[@class="il_img"]//img/@src')
print(img_url)

for img in img_url:
    root_dir = 'img'
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)

    filename = img.split('/')[-1]
    # print(filename)
    dir = "./" + root_dir + "/" + filename
    # print(dir)
    """
    获取到页面中封面图的url与实际不符，列封面中的url为：
    //img.ivsky.com/img/tupian/li/201904/22/lantian_baiyun-002.jpg
    
    而实际的地址为：
    //img.ivsky.com/img/tupian/li/201904/22/lantian_baiyun-002.jpg
    
    则所有获取到的地址均需要手动拼接图片的完整url。
    """
    request.urlretrieve("https:" + img, dir, Schedule)