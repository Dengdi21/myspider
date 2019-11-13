"""
构建代理集群
每次访问服务器，随机抽取一个代理
抽取可以使用 random.choice
"""

# 构建代理群
# 每次访问，随机选取代理


from urllib import request, error

# 使用代理

proxy_list = [
    {"http": "101.50.1.2:80"},
    {"http": "58.240.172.110:3128"},
    {"http": "124.193.51.249:3128"},
    {"http": "120.199.64.163:8081"},
]

# 创建ProxyHandler
proxy_handler_list = []
for proxy in proxy_list:
    proxy_handler = request.ProxyHandler(proxy)
    proxy_handler_list.append(proxy_handler)

# 创建Opener

opener_list = []
for proxy_handler in proxy_handler_list:
    opener = request.build_opener(proxy_handler)
    opener_list.append(opener)

import random
url = 'http://www.baidu.com'

# 如果现在可以访问url，则使用代理服务器
try:
    # 安装Opener
    opener = random.choice(opener_list)
    request.install_opener(opener)

    # 访问
    rsp = request.urlopen(url)
    html = rsp.read().decode('utf-8')
    print(html)
except error.URLError as e:
    print(e)
except Exception as e:
    print(e)
