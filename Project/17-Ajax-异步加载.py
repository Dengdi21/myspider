"""
Ajax异步加载

举例：
https://www.pexels.com/

分析：打开网页分析，边加载网页边得到网页更新内容，以及在查看器中新增了
许多url，分析url可得出规律。

https://cat.pexels.com/?page1
https://cat.pexels.com/?page2
https://cat.pexels.com/?page3

"""

import requests
from bs4 import BeautifulSoup

headers = {
    'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) \
                                   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

urls = ["https://cat.pexels.com/?page{}".format(i) for i in range(2, 3)]

print(urls)

photos = []
for url in urls:
    response = requests.get(url, headers=headers)
    html = response.text
    print(html)

    soup = BeautifulSoup(html, 'lxml')

    imgs = soup.select('article > a > img')

    for img in imgs:
        photo = img.get('src')
        if photo.endswith('350'):
            photos.append(photo)
            print(photo)

# 图片下载
path = './'
import re

for item in photos:
    data = requests.get(item, headers=headers)
    photo_name = re.findall('\d+\/(.*?)\?', item)

    print(photo_name[0])

    if photo_name:
        fp = open(path+"/"+photo_name[0], 'wb')
        fp.write(data.content)
        fp.close()








