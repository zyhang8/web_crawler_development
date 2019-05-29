"""
直接知乎搜索问题，然后复制整个URL：

示例：
1、Key_word 中输入要在知乎搜索的关键词

2、运行即可
"""
from urllib import parse
import json
import time
import requests
from bs4 import BeautifulSoup

proxies = {"http": "113.78.255.243:8118", "https": "182.88.15.168:1080", }

# 云主机 跨云管理 云管理 私有云 混合云
Key_word = parse.quote('广东春节习俗', safe='/', encoding=None, errors=None)


# url = 'https://www.zhihu.com/search?type=content&q=%E5%A0%A1%E5%9E%92%E6%9C%BA'   # 堡垒机
url = 'https://www.zhihu.com/search?type=content&q={}'.format(Key_word)     # 云管理

print(url)

MacbookPro_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}

# wb_data = requests.get(url, headers=MacbookPro_headers, proxies=proxies)
wb_data = requests.get(url, headers=MacbookPro_headers)

soup = BeautifulSoup(wb_data.text, 'lxml')

URL_list = []
for i in range(5, 100000, 10):
    """
    limit = 每次返回的条数（上线10）
    offset = 页面条数（递增10，首个为5）
    """
    URL = "https://www.zhihu.com/api/v4/search_v3?t=general&q={}&correction=1&offset={}&limit=10".format(Key_word, i)
    print('将要请求的URL', URL)
    URL_list.append(URL)

url_list = []

for url in URL_list:
    time.sleep(4)
    # wb_data = requests.get(url,headers=MacbookPro_headers,proxies=proxies)
    wb_data = requests.get(url,headers=MacbookPro_headers)
    wb_data = json.loads(wb_data.text)
    if wb_data['data']:
        for i in wb_data['data']:
            for k, v in i.items():
                if k == 'object':
                    try:
                        if v['question']['id']:
                            object_id = v['id']
                            question_id = v['question']['id']
                            question_url = 'https://www.zhihu.com/question/{}/answer/{}'.format(question_id, object_id)
                            url_list.append(question_url)
                            print('问题链接：', question_url)
                    except Exception:
                        article_url = 'https://zhuanlan.zhihu.com/p/'+str(v['id'])
                        url_list.append(article_url)
                        print('文章链接：', article_url)
    else:
        break

ok_link = []
print('爬取到的URL：', len(url_list))

for i in url_list:
    url = i
    print('正在测试该链接的有效性：', url)
    try:
        # r = requests.get(url, headers=MacbookPro_headers, timeout=30,proxies=proxies)
        r = requests.get(url, headers=MacbookPro_headers, timeout=30)
        r.raise_for_status()  # 如果返回的状态码不是200，则引发HTTPerror异常
        if url not in ok_link:
            ok_link.append(url)
    except Exception as e:
        print(e, url)
        print('              ')


print('有效URL', len(ok_link))


"""
第三步：循环打印最后的URL
"""
for i in ok_link:
    print(i)