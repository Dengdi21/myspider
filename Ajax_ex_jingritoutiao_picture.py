import os
from hashlib import md5
import requests
from urllib.parse import urlencode


def get_one_page(offset):

    headers = {
        "Accept": "application / json, text / javascript",
        "Accept - Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "__tasessionId=ownx5miwv1567686040369; csrftoken=a0633b00a7eb984349d529bb9b445da2; tt_webid=6733160252969944587; s_v_web_id=a027a1501f46fc367369e0e19892a122",
        "Host": "www.toutiao.com",
        "TE": "Trailers",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0",
        "X-Requested-With": "XMLHttpRequest"
    }

    params = {
        "aid" : '24',
        "app_name": "web_search",
        "offset":   offset,
        "format": "json",
        "keyword": "街拍",
        "autoload": "true",
        "count": "20",
        "en_qc": "1",
        "cur_tab": "1",
        "from": "search_tab",
        "pd": "synthesis",

    }
    url = "https://www.toutiao.com/api/search/content/?" + urlencode(params)
    print(url)

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print(response.text)
            return response.json()

    except requests.ConnectionError:
        return None


def get_images(json):
    print(type(json))
    if json.get('data'):
        print(json.get('data'))
        for item in json.get("data"):
            title = item.get("title")
            images = item.get('image_datail')
            for image in images:
                yield {
                    "image": image.get('url'),
                    'title': title
                }


def save_image(item):
    if not os.path.exists(item.get("title")):
        os.mkdir(item.get("title"))

        try:
            response = requests.get(item.get('image'))
            if response.status_code == 200:
                file_path = '{0}/{1}.{2}'.format(item.get("title"), md5(response.content).hexdigest(), 'jpg')
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(response.content)

                else:
                    print('已下载：', file_path)
        except requests.ConnectionError:
            print('保存失败')


from multiprocessing.pool import Pool


def main(offset):
    json = get_one_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START = 1
GROUP_END = 3

if __name__ == '__main__':
    pool = Pool()
    groups = [x * 20 for x in range(GROUP_START, GROUP_END + 1)]
    print(groups)

    pool.map(main, groups)

    pool.close()
    pool.join()



