"""
爬取糗事百科
1.需要使用requests爬取页面，用xpath，re提取数字
2.可提取信息是用户头像连接，段子内容，点赞，好评次数
3.保存到json文件中
"""

"""
1.down下页面
2.利用xpath提取信息
3.保存文件
"""

import requests

from lxml import etree

url = "https://www.qiushibaike.com/8hr/page/1/"

headers = {
    'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) \
                                   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
# 网页源代码
rsp = requests.get(url, headers=headers)
html = rsp.text

print(html)

html = etree.HTML(html)
rst = html.xpath("//div[contains(@id, 'qiushi_tag')]")

for r in rst:
    print(type(r))
    print(r.tag)
    print(r)
