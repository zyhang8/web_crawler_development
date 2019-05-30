import requests
from bs4 import BeautifulSoup

url = 'http://www.ioc-sealevelmonitoring.org/station.php?code=abas'
req = requests.get(url, {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
soup = BeautifulSoup(req.text, 'lxml')
print(list(soup.find_all(name="td", attrs={"class": "nice"}))[2].string.strip())
print(list(soup.find_all(name="td", attrs={"class": "nice"}))[3].string.strip())
print(list(soup.find_all(name="td", attrs={"class": "nice"}))[8].string.strip())
print(list(soup.find_all(name="td", attrs={"class": "nice"}))[9].string.strip())
with open("fourth_test_ports.txt", 'w', encoding='utf-8') as f:
    f.write(list(soup.find_all(name="td", attrs={"class": "nice"}))[2].string.strip() + ' ' +
            list(soup.find_all(name="td", attrs={"class": "nice"}))[3].string.strip() + ' ' +
            list(soup.find_all(name="td", attrs={"class": "nice"}))[8].string.strip() + ' ' +
            list(soup.find_all(name="td", attrs={"class": "nice"}))[9].string.strip())
