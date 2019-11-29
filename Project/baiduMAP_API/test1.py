"""

注册百度地图API账号并进行开发者认证
目标：获取全国公园信息并保存在mysql数据库中

地点检索详情链接
http://api.map.baidu.com/place/v2/detail?uid=435d7aea036e54355abbbcc8&output=json&scope=2&ak=您的密钥 //GET请求

基础地址
http://api.map.baidu.com/place/v2/detail?

参数：
query :公园
region ：成都
scope ：2
page_size ：20
ak：密匙
"""

import requests


def get_json(loc, page_num=0):
    headers = {
        'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0'
    }
    data = {
        'query': '公园',
        'region': '成都',
        'scope': 2,
        'page_size': 20,
        'page_num': page_num,
        'output': "json",
        'ak': 'gXaG3THhX20020c2T8eUMIHHeo8X528GQ'
    }

    url = "http://api.map.baidu.com/place/v2/search"
    res = requests.get(url, params=data, headers=headers)
    decodejson = res.text

    return decodejson

if __name__ == '__main__':
    a = get_json('成都市')
    print(a)

