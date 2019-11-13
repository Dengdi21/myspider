# from urllib import request, parse

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 1
# data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf8')
#
# response = request.urlopen('http://httpbin.org/post', data=data)
#
# print(response.read())


# 2
# from urllib.parse import urlparse
#
# result = urlparse('http://www.baidu.com/index.html;url?id=5#comment')
# print(type(result), result)


# 3
# from urllib.parse import urlencode
#
# params = {
#   'name': 'germy',
#   'age': 22
# }
#
# base_url = 'http://www.baidu.com?'
# url = base_url + urlencode(params)`
# print(url)

# 4
# from urllib.parse import quote, unquote
#
# keyword = '加油'
# url = 'http://www.baidu.com/s?wd=' + quote(keyword)
#
# print(url)
#
# unurl = 'http://www.baidu.com/s?wd=%E5%8A%A0%E6%B2%B9'
# print(unquote(unurl))


# 5
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))


