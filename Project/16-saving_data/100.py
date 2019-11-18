import time
import requests
import re
import json
from requests.exceptions import RequestException


def get_one_page(url):
    try:
        headers = {
            'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) \
                            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.text

        return None

    except RequestException:
        return None


def main(offset):

    url = "https://maoyan.com/board/4?offset={}".format(str(offset))
    print('已获取第{}页url'.format(offset))
    html = get_one_page(url)

    print('访问成功。\n正在解析......')
    for item in pase_one_page(html):
        # print(item)

        print('解析成功。\n正在写入......')
        write_to_file(item)
        print('写入成功')

    # print(html)


def pase_one_page(html):
    pattern = re.compile(
        "<dd>.*?board-index.*?>(.*?)</i>.*?data-src=\"(.*?)\".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</P>.\
        *?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?</dd>", re.S
    )

    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:0],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6],
        }


def write_to_file(content):
    with open('./result.txt', 'a', encoding='utf-8') as f:
        # print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    for i in range(10):
        print('准备第{}页'.format(i))
        main(offset=i*10)
        time.sleep(1)