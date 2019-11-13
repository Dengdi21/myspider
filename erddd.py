import requests
from urllib.parse import urlencode

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


url = "http://m10.music.126.net/20191013161154/417de82c06069ef0ea098f836ff4853c/ymusic/b854/e1ff/e7c1/653c638e24580e2869184c592a370056.mp3"

response = requests.get(url, headers=headers)
with open("./music.mp3", 'wb') as f:
    f.write(response.content)



