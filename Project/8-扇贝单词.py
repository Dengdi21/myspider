"""
扇贝单词
1.把python单词列表download下来
2.主要练习xpath
3.理论上不需要登录
"""

from urllib import request
from lxml import etree

import json

words = []

def shanbei(page):

    url = "https://web.shanbay.com/wordsweb/#/words-table"
    print(url)

    rsp = request.urlopen(url)

    html = rsp.read()
    # 解析html
    html = etree.HTML(html)

    tr_list = html.xapath("//tr")

    # 遍历tr_list,获取单个单词
    for tr in tr_list:
        word = {}
        strong = tr.xpath('./strong')
        if len(strong):
            name = strong[0].text.strip()
            word['name'] = name

            print(name)

        td_content = tr.xpath('./td[class="span10"]')

        if len(td_content):
            content = td_content[0].text.strip()
            word['content'] = content

            print(content)
            
        if word != {}:
            words.append(word)


if __name__ == '__main__':
    shanbei(2)


