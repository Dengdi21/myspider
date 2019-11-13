"""
爬取腾讯招聘
https://hr.tencent.com/position.php?&start10#a
"""

from bs4 import BeautifulSoup
from urllib import request

def qqhr():
    # 获取页面
    url = "https://hr.tencent.com/position.php?&start10#a"

    rsp = request.urlopen(url)
    html = rsp.read()

    # 获取内容
    # 用bs4解析
    soup = BeautifulSoup(html, 'lxml')

    # 创建css选择器，得到相应tag
    tr1 = soup.select("tr[class='even']")
    tr2 = soup.select("tr[class='odd]")
    trs = tr1 + tr2

    for tr in trs:
        # 获取文本
        name = tr.select('td a')[0].get_text()
        print(name)
        # 获取标签
        href = tr.select('td a')[0].attrs['href']
        print(href)
        catalong = tr.select('td')[1].get_text()
        print(catalong)
        location = tr.select('td')[3].get_text()
        print(location)
        print('==' * 100)

if __name__ == '__main__':
    qqhr()