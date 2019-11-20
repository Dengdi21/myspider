"""
网易云音乐歌手信息

https://music.163.com/discover/artist/cat?id=4001

歌手类别：
id = 4001
initial = 0

热门，A-Z，其他：
init = [-1, 65-90, 0]
"""
import requests
from bs4 import BeautifulSoup

import csv


def get_artists(url):
    headers = {
        'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) \
                                       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    html = r.text

    soup = BeautifulSoup(html, 'lxml')

    items = soup.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'})
    for item in items:
        artist_name = item.sting.strip()
        artist_id = item['href'].strip()
        print(artist_id, artist_name)
        csv_save(artist_id, artist_name)


# 写入csv
def csv_save(id, name):
    try:
        writer.writerow((id, name))
    except Exception as e:
        print('写入失败')
        print(e)


if __name__ == '__main__':
    id_list = [1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 7001, 7002, 7003, 4001, 4 - -2, 4003]
    init_list = [-1, 0] + [x for x in range(65, 91)]
    # print(init_list)
    csvfile = open('music_163_artist.csv', 'a')
    writer = csv.writer(csvfile)
    writer.writerow(('artist_id', 'artist_name'))

    for i in id_list:
        for j in init_list:
            url = "https://music.163.com/discover/artist/cat?id={0}&initial={1}".format(i, j)

            get_artists(url)