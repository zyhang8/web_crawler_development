import requests
from lxml import etree


USER = ''    # 隐藏的用户名和密码，哈哈
PASSWORD = ''


# 创建Login类，封装模拟登陆
class Login(object):
    def __init__(self):
        self.headers = {
            'Host': 'github.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64;rv:62.0) Gecko/20100101 Firefox/62.0',
            # 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36',
            # 使用谷歌浏览器的User-Agent时，返回的token为空列表，但使用火狐则成功，这是为什么？
        }
        self.login_url = 'https://www.github.com/login'  # 登陆页面的URL
        self.profile_url = 'https://www.github.com/settings/profile'  # 个人详情页URL
        self.session = requests.Session() # requests.Session()帮我们维持一个会话，自动处理Cookie

    # 获取authentici_token
    def get_token(self):
        response = self.session.get(url=self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)  # 解析HTML对象
        print(selector.xpath('//*[@id="login"]/form/input[2]/@value'))  # 提取所有id属性为login元素下的form元素的第二个input元素的value属性所对应的值
        token = selector.xpath('//*[@id="login"]/form/input[2]/@value')
        return token

    # 登陆至个人详情页，获取信息
    def login(self, email, passwd):
        form_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.get_token(),
            'login': email,
            'password': passwd
        }
        response = self.session.get(url=self.profile_url, data=form_data, headers=self.headers)
        print(response.status_code)
        if response.status_code == 200:
            self.dynamics(response.text)

        response = self.session.post(url=self.profile_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def dynamics(self, html):
        pass


    def profile(self, html):
        pass


if __name__ == '__main__':
    login = Login()
    login.login(USER, PASSWORD)