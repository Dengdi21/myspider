import requests

# 1
# r = requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(r.text)
# print(type(r.text))
# print(r.cookies)


# 2
# data = {
#     'name': 'germey',
#     'age': 22
# }
#
# rep = requests.get("http://httpbin.org/get", params=data)
# print(type(rep))
# print(rep.text)
# print(type(rep.text))
# print(rep.json())
# print(type(rep.json()))


# 3.二进制文件
# r3 = requests.get("https://github.com/favicon.ico")
# s = r3.content
# print(r3.text)
# print(type(s))
# print(s)
#
# with open('./test.ico', 'wb') as f:
#     f.write(s)
# f.close()


# 4.post
# data = {
#     'name': 'germey',
#     'age' : 33
# }
#
# r4 = requests.post("http://httpbin.org/post", data=data)
#
# print(r4.text)


# 5.文件上传
# files = {
#     'files': open('./test.ico', 'rb')
# }
#
# r5 = requests.post("http://httpbin.org/post", files=files)
#
# print(r5.text)


# 6.Cookies

# 获取cookies
# r6_1 = requests.get("https://www.baidu.com")
# print(r6_1.cookies)
#
# for key, value in r6_1.cookies.items():
#     print(key + '=' + value)


# 7.会话维持 Session
# 7.1
# requests.get("http://httpbin.org/cookies/set/number/123456789")
#
# r7_1 = requests.get("http://httpbin.org/cookies")
#
# print(r7_1.text)  # 空
#
# # 7.2
# s7 = requests.Session()
#
# s7.get("http://httpbin.org/cookies/set/number/123456789")
# r7_2 = s7.get("http://httpbin.org/cookies")
#
# print(r7_2.text)


# 8.SSL证书
# response = requests.get('https://www.12306.cn')
# print(response.status_code)
#
# # 设置
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)


# 9.代理设置

# proxies = {
#     "http": "http://10.10.1.1.10:3128",
#     "https": "http://10.10.1.1.10:1080"
# }
#
# requests.get("https://www.taobao.com", proxies=proxies)


# 10.超时设置
# r10 = requests.get("https://www.taobao.com", timeout=2)
# print(r10)
#
# r10 = requests.get("https://www.taobao.com", timeout=(5, 10, 30))  # (连接，读取，超时)


# 11.身份认证
# from requests.auth import HTTPBasicAuth

r11 = requests.get('http://localhost:5000', auth=('username', 'password'))

print(r11.status_code)




