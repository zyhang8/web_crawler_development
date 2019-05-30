import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient("127.0.0.1", 27017)
db = client['tide']
collection = db['tide']
num_time = 0  # 定义条数的初始值
add_he = 0
num_invalid_time = 0
num_even = 0
num_odd = 0
url = 'https://www.tide-forecast.com/locations/Chenghua/tides/latest'
req = requests.get(url, {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
soup = BeautifulSoup(req.text, 'lxml')
i = 0
j = 0
w = 0
# y = 0
k_add = 0
list_date = []  # 日期数量
list_tr = []  # tr数量
list_even_num = []  # 日期even数量
list_odd_num = []  # 日期odd数量
num_td = []  # 日期td数量
valid_tide = []  # 有效tide
num_date = len(list(soup.find_all(name="th", attrs={"class": "date"})))  # 日期数量
for tap_a in soup.find_all(name='tr', attrs={"class": True}):
    # print(' '.join(tap_a['class']))
    list_tr.append(' '.join(tap_a['class']))
tr_len = len(list_tr)
list_tr.append('none')
# print(list_tr)
# print(' '.join(list_even))
# print(tr_len)
if list_tr[0] == 'even':
    list_even_num = list_tr
    for j in range(0, tr_len):
        # print(list_tr[j])
        num_even += 1
        if j <= tr_len - 1 and list_tr[j] != list_tr[j + 1]:
            num_td.append(num_even)
            # print(num_even)
            num_even = 0
    # print(num_td)
elif list_tr[0] == 'odd':
    list_odd_num = list_tr
    for j in range(0, tr_len):
        # print(list_tr[j])
        num_odd += 1
        if j <= tr_len - 1 and list_tr[j] != list_tr[j + 1]:
            num_td.append(num_odd)
            # print(num_even)
            num_odd = 0
add_tr = [0] * (len(num_td))  # 前面元素之和
for t in range(1, len(num_td)):
    for m in range(0, t):
        # print(num_td[m])
        add_he += num_td[m]
        # print(add_he)
        # print("m:", m)
        # print("l:", t)
    add_tr[t] = add_he
    add_he = 0
for i in range(0, num_date):
    list_date.append(list(soup.find_all(name="th", attrs={"class": "date"})[i]))
    print((''.join(list_date[i])).strip())  # 日期
    y = 0
    for k in range(0, num_td[i]):
        # print(num_td[i])
        # print(k)
        if list(soup.find_all(name="td", attrs={"class": "level metric"}))[add_tr[i] + k].string is not None:
            # y = 0
            y += 1
            # print(k)
            # tide = {}
            # tide['_id'] = (''.join(list_date[i])).strip()
            # tide['time'] = list(soup.find_all(name="td", attrs={"class": "time"}))[add_tr[i] + k].string.strip()
            # tide['time-zone'] = list(soup.find_all(name="td", attrs={"class": "time-zone"}))[
            #                             add_tr[i] + k].string.strip()
            # tide['level metric'] = list(soup.find_all(name="td", attrs={"class": "level metric"}))[
            #                                add_tr[i] + k].string
            # tide['imperial'] = list(soup.find_all(name="span", attrs={"class": "imperial"}))[w].string.strip()
            # Chenghua['imperial'] = list(soup.find_all(name="td", attrs={"class": "tide"}))[2 * w + 1].string.strip()
            db["Chenghua"].insert(
                {"_id": (''.join(list_date[i])).strip() + str(y),
                 "date": (''.join(list_date[i])).strip(),
                 "time": list(soup.find_all(name="td", attrs={"class": "time"}))[add_tr[i] + k].string.strip(),
                 "time-zone": list(soup.find_all(name="td", attrs={"class": "time-zone"}))[
                     add_tr[i] + k].string.strip(),
                 "level metric": list(soup.find_all(name="td", attrs={"class": "level metric"}))[add_tr[i] + k].string,
                 "imperial": list(soup.find_all(name="span", attrs={"class": "imperial"}))[w].string.strip(), "tide":
                     list(soup.find_all(name="td", attrs={"class": "tide"}))[2 * w + 1].string.strip()})
            print(list(soup.find_all(name="td", attrs={"class": "time"}))[add_tr[i] + k].string.strip())
            print(list(soup.find_all(name="td", attrs={"class": "time-zone"}))[add_tr[i] + k].string.strip())
            print(list(soup.find_all(name="td", attrs={"class": "level metric"}))[add_tr[i] + k].string)
            print(list(soup.find_all(name="span", attrs={"class": "imperial"}))[w].string.strip())
            print(list(soup.find_all(name="td", attrs={"class": "tide"}))[2 * w + 1].string.strip())
            # print(add_tr[i] + k + 1)
            w += 1

# tag_soup = soup.find(name="td", attrs={"class": ""})
# print(list(soup.tybody.conetents)[0].attrs['class'])
# print(list(soup.find_all(name="tr", attrs={"class": "even"||"even"}))[0].attrs['class'])
# print(soup.select('.even.odd'))
# print(soup.select('.even'))

#     if list(soup.find_all(name="td", attrs={"class": "level metric"}))[i].string is not None:
#         num_invalid_time = len(list(soup.find_all(name="td", attrs={"class": "time"})))
#         print(list(soup.find_all(name="td", attrs={"class": "time"}))[i].string.strip())
#         print(num_invalid_time)
#  print(num_date)
# print(list(soup.find_all(name="td", attrs={"class": "time"}))[i].string.strip())
# print(list(soup.find_all(name="td", attrs={"class": "time-zone"}))[i].string.strip())
# print(list(soup.find_all(name="td", attrs={"class": "level metric"}))[i].string)
# print(list(soup.find_all(name="td", attrs={"class": "level"}))[i].string)
# print(list(soup.find_all(name="td", attrs=None)))

# for i in range(0, num):
# for td in soup.find(name="tr", attrs={"class": "even"}):
