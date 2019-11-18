import requests
import csv
from lxml import etree
import re

headers = {
    "User-Agent": "Mozilla / 5.0(Macintosh;IntelMacOSX10_14_2) AppleWebKit / \
    537.36(KHTML, likeGecko) Chrome / 78.0.3904.87Safari / 537.36"}

url = 'http://www.seputu.com/'
rsp = requests.get(url, headers=headers)

html = etree.HTML(rsp.text)

div_nulus = html.xpath('//*[@class="mulu"]')

rows = []
for div_mulu in div_nulus:
    div_h2 = div_mulu.xpath('.//div[@class="mulu-title"]/center/h2/text()')
    # print(div_h2)

    if len(div_h2)>0:
        h2_title = div_h2[0]
        list1 = []
        a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            href = a.xpath('./@href')[0]
            title = a.xpath('./@title')[0]

            pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
            match = pattern.search(title)

            if match != None:
                data = match.group(1)
                real_title = match.group(2)
                # print(data, real_title)

                content = (h2_title, real_title, href, data)
                # print(content)
                rows.append(content)


# 写入csv
headers = ['title', 'real_title', 'href', 'data']

with open('daomubij.csv', 'a', newline='', encoding='utf-8') as f:
    csv_f = csv.writer(f)
    csv_f.writerow(headers)
    csv_f.writerows(rows)