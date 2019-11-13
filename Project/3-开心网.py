"""
登录开心网
利用cookie
免除ssl
"""
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
"""
步骤
1.找到登录入口
    找到登录表单，提交网址为 https://security.kaixin001.com/login/login_post.php
    相应的用户和登录密码对应名称为email，password
    
2.构造opener

"""
from urllib import  request, parse

from http import cookiejar
cookie = cookiejar.CookieJar()
cookie_hendler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(http_handler, https_handler, cookie_hendler)

def login():
    login_url = "https://security.kaixin001.com/login/login_post.php"

    data = {
        "email": "18512800525",
        "password": "D872360311d"
    }
    # 对post的data内容进行编码
    data = parse.urlencode(data)

    # 请求头
    headers = {
        "Content-length": len(data),
        'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) \
                                   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

    # 构建请求
    req = request.Request(login_url, data=data.encode(), headers=headers)

    rsp = opener.open(req)

    html = rsp.read()
    html = html.decode()
    print(html)

def gethomepage():
    """
    获取主页
    """
    base_url = "http://www.kaixin001.com/home/?_profileuid=181888979&t=57"
    rsp = opener.open(base_url)
    html = rsp.read()
    html = html.decode()

    print(html)


if __name__ == '__main__':
    login()
    print("*" * 200)
    gethomepage()