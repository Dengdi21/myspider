"""
去张继科把
1.主页: https://tieba.baidu.com/f?kw=张继科
2.第二页网址：https://tieba.baidu.com/f?kw=张继科&fr=ala0&tpl=50
3.第三页网址：https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=100
4.第四页网址：https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=150
5.第五页网址：https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=150
由此找到规律

1，准备参数字典
    字典包含三部分 kw，ie, pn
2，使用parse构建完整url
3，使用for循环下载
"""

from urllib import request, parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':

    qs = {
        "kw": "张继科",
        "ie": "utf-8",
        "pn": 0
    }

    urls = []
    baseurl = "https://tieba.baidu.com/f?"
    # 前5页
    for i in range(5):
        pn = i*50
        qs["pn"] = str(pn)
        # 把qs编码后和基础url进行拼接后放入urls列表中
        urls.append(baseurl + parse.urlencode(qs))
    print(urls)

    for url in urls:
        rsp = request.urlopen(url)
        html = rsp.read().decode("utf-8")
        print(url)
        print(html)