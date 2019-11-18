"""
python对json文件的操作分为编码和解码

dumps  字符串
dump   json对象  可以通过fp文件流写入文件


解码：
load
loads 字符串操作
"""

# 知识点
# import json
#
# str1 = "[{'username': 'dachang,', 'age': 19}]"
# print(type(str1))
#
# json_str = json.dumps(str1, ensure_ascii=False)
# print(json_str)
# print(type(json_str))
#
# new_str = json.loads(json_str)
# print(new_str)
# print(type(new_str))

# 举例
import requests
import json
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla / 5.0(Macintosh;IntelMacOSX10_14_2) AppleWebKit / \
    537.36(KHTML, likeGecko) Chrome / 78.0.3904.87Safari / 537.36"}

url = 'http://www.seputu.com/'
rsp = requests.get(url, headers=headers)
# print(rsp.text)

soup = BeautifulSoup(rsp.text, 'lxml')

content = []
for mulu in soup.find_all(class_= "mulu"):
    # print(mulu)
    # 标题
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.string
        print(h2_title)

        list1 = []

        # 获取标题内容url地址
        for a in mulu.find(class_="box").find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            # print(href)
            # print(box_title)

            list1.append({'href': href, 'box_title': box_title})

        content.append({'title': h2_title, 'content': list1})


with open('daomubiji.json', 'a', encoding='utf-8') as f:
    json.dump(content, fp=f, indent=4, ensure_ascii=False)
