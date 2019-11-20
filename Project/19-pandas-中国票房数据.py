"""
1. 安装pandas numpy
2.或者直接安装ancomda（集成环境）
3.利用pandas保存数据

抓取中国票房网数据
url= 'www.cbooo.cn'
"""

import pandas as pd

import requests
from bs4 import BeautifulSoup

url = "http://www.cbooo.cn/year?year=2019"

datas = requests.get(url).text

soup = BeautifulSoup(datas, 'lxml')

movies_html = soup.find_all('table', {'id': 'tbContent'})[0]
# print(movies_html)

movies = movies_html.findAll('tr')
# print(movies)

names = []
hrefs = []
types = []
boxes = []
box_avgs = []
pre_avgs = []
countries_s = []
data_s = []

for movie in movies[1:]:
    name = movie.find_all('td')[0].a.get('title')
    href = movie.find_all('td')[0].a.get('href')
    type = movie.find_all('td')[1].string
    box = movie.find_all('td')[2].string
    box_avg = movie.find_all('td')[3].string
    pre_avg = movie.find_all('td')[4].string
    countries = movie.find_all('td')[5].string
    data = movie.find_all('td')[6].string
    # print(name, href, type, box, box_avg, pre_avg, countries, data)
    names.append(name)
    hrefs.append(href)
    types.append(type)
    boxes.append(box)
    box_avgs.append(box_avg)
    pre_avgs.append(pre_avg)
    countries_s.append(countries)
    data_s.append(data)

df = pd.DataFrame(
    {'name': names,
     'href': hrefs ,
    'type':  types,
    'box': boxes,
    'box_avg': box_avgs,
    'pre_avg':pre_avgs,
    'countries':countries_s,
    'data':data_s}
)

print(df.head())

# 数据存储
df.to_csv('movies.csv')


