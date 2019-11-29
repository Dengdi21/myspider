"""

"""
import requests
from lxml import etree
from Project.data_to_mongodbAPI import MongoAPI

def spider(url):
    """
    请求
    :param url:
    :return:
    """
    headers = {
        'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) \
                                          AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    req = requests.get(url, headers=headers)

    html = req.text
    html = etree.HTML(html)

    return html


def parse(html):
    """
    解析
    :param html:
    :return:
    """
    # 标题(可舍去，因为不同的颜色标题可能不存在详情页，导致标题数量与下面的详情页连接个数不一致，解决方法为先取详情页，再从详情页中获取标题)
    titles = html.xpath('//ul[@class="for-list"]//div[@class="titlelink box"]/a[@class="truetit"]/text()')
    # print(titles)

    # 详情页连接
    parse_hrefs =  html.xpath('//ul[@class="for-list"]//div[@class="titlelink box"]/a[@class="truetit"]/@href')
    hrefs = ['https://bbs.hupu.com' + href for href in parse_hrefs]
    print(hrefs)

    # 获取标题
    titles_list = []
    for href in hrefs:
        titles_list.append(title(href))

    # 获取作者
    aothors = html.xpath('//div[@class="author box"]/a[@class="aulink"]/text()')

    # 获取发布时间
    times = html.xpath('//div[@class="author box"]/a[2]/text')

    # 获取回复数和发布时间
    datas = html.xpath('//ul[@class="for-list"]/li/span[@class="ansour box"]/text()')
    datas = [x.split('\xa0/\xa0') for x in datas]
    # 回复数
    replies = [x[0] for x in datas]
    # 浏览数
    brows = [x[1] for x in datas]

    # 最后回复时间
    last_times = html.xpath('//div[@class="endreply box"]/a/text()')

    # 最后回复人
    last_names = html.xpath('//div[@class="endreply box"]/soan[@class="endauthor"]/text()')

    # 数据打包
    items = zip(titles_list, hrefs, aothors, times, replies, brows, last_times, last_names)

    return items


# 获取标题
def title(href):
    html = spider(href)
    t = html.xpath('//div[@class="bbs-hd-h1"]/h1/text()')
    print(t)
    return t


# 数据存储
def data_storage(items):
    print(items)
    # 实例化数据库接口
    hupu_post = MongoAPI("localhost", 27017, "new_hupu", "post")

    # titles_list, hrefs, , times, replies, brows, last_times, last_names
    for item in items:
        hupu_post.add({
            "titles_list": item[0],
            "hrefs, aothors": item[1],
            "aothors": item[2],
            "times": item[3],
            "replies": item[4],
            "brows": item[5],
            "last_times": item[6],
            "last_names": item[7],
        })
    print('存储完成')

def main():
    url = "https://bbs.hupu.com/nba"
    html = spider(url)

    data_storage(parse(html))


if __name__ == '__main__':
   main()