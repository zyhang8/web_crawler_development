import requests
from bs4 import BeautifulSoup

num = 0  # 定义条数的初始值
url = 'https://www.tide-forecast.com/locations/Paradwip-India/tides/latest'
req = requests.get(url, {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
soup = BeautifulSoup(req.text, 'lxml')
# 找到所有p标签中的内容并存放在xml这样一个类似于数组队列的对象中
xml = soup.find_all(name='th.date', class_='')
# 利用循环将xml[]中存放的每一条打印出来
f = open("second.txt", "w+")
for td in soup.select('th'):
    print(td.get_text(),file=f)
    print(td.get_text())
    for td in soup.select('td'):
        print(td.get_text(), file=f)
        print(td.get_text())
f.close()
