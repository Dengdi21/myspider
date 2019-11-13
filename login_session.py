import requests
from lxml import etree


class Login(object):
    def __init__(self):
        """
        初始化变量，Session用来维持一个会话
        """
        self.headers = {
            "Referer": 'https:github.com',
            'User-Agent':  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0",
            'Host': 'github'
        }

        self.login_url = 'https://github.com/Login'
        self.post_url = 'https:://github.com/session'
        self.logined_url = 'https:://github.com/settings/profile'

        self.session = requests.Session()

    def taken(self):
        """
        获取authenticity_token字段
        :return: authenticity_token
        """
        response = self.session.get(self.login_url, headers=self.headers)
        selector =  etree.HTML(response.text)

        token = selector.xpath('//div//input[2]/@value')[0]

        return token

    def dynamics(self, html):
        selector = etree.HTML(html)
        dynamics = selector.xpath('//div[conttains(@class, "news")]//div[contains(@class, "alert")]')
        for item in dynamics:
            dynamics = ''.join(item.xpath('.//div[@class="title"]//text()')).strip()
            print(dynamics)

    def profile(self, html):
        selector = etree.HTML(html)
        name = selector.xpath('//input[@id="user_prifile_name"]/@value')[0]
        email = selector.xpath('//select[@id=user_prifile_emial]/option[@value!=""]/text()')
        print(name, email)

    def login(self, email, password):
        """
        模拟登陆
        :return:
        """
        post_data = {
            'commit': "Sign in",
            'utf8': '',
            'authenticity_token': self.taken(),
            'login': email,
            'password': password
        }

        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)


if __name__ == '__main__':
    login = Login()

    login.login(email='16284691807@163.com', password='password')
