# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 21:40
# @Author  : zyh
# @File    : all_data.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://tides4fishing.com'
req = requests.get(url, {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
soup = BeautifulSoup(req.text, 'lxml')
with open("allports_t4f.csv", "w") as a:
    writer = csv.writer(a)
    writer.writerow(["Station Name", "lat", "lon"])
    for continent_url in soup.find_all(name='a', attrs={"class": "sitio_continente_txt"}):
        req = requests.get(continent_url['href'],
                           {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
        soup = BeautifulSoup(req.text, 'lxml')
        for country_url in soup.find_all(name='a', attrs={"class": "sitio_reciente_a"}):
            req = requests.get(country_url['href'],
                               {
                                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
            soup = BeautifulSoup(req.text, 'lxml')
            for city_url in soup.find_all(name='a', attrs={"class": "sitio_reciente_a"}):
                req = requests.get(city_url['href'],
                                   {
                                       'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
                soup = BeautifulSoup(req.text, 'lxml')
                port_len = len(soup.find_all(name='div', attrs={"class": "sitio_estacion"}))
                for port in range(0, port_len):
                    port_url = list(soup.find_all(name='a', attrs={"class": "sitio_estacion_a"}))[port]
                    if soup.find_all(name='a', attrs={"class": "sitio_reciente_a"}):
                        print(soup.find_all(name='a', attrs={"class": "sitio_reciente_a"}))
                        for city_url in soup.find_all(name='a', attrs={"class": "sitio_reciente_a"}):
                            # print(city_url)
                            req = requests.get(city_url['href'],
                                               {
                                                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
                            soup = BeautifulSoup(req.text, 'lxml')
                            port_len = len(soup.find_all(name='a', attrs={"class": "sitio_estacion_a"}))
                            for port in range(0, port_len):
                                port_url = list(soup.find_all(name='a', attrs={"class": "sitio_estacion_a"}))[port]
                                if list(soup.find_all(name='a', attrs={"class": "sitio_estacion_a"}))[port] is not None:
                                    print(port_url['href'])
                                    print(port_url['href'].split('/')[-1])
                                    print(list(
                                        soup.find_all(name="span", attrs={"class": "sitio_estacion_coordenadas_N"}))[
                                              port].get_text())
                                    print(list(
                                        soup.find_all(name="span", attrs={"class": "sitio_estacion_coordenadas_W"}))[
                                              port].get_text())
                                    writer.writerows([[port_url['href'].split('/')[-1],
                                                       list(soup.find_all(name="span",
                                                                          attrs={
                                                                              "class": "sitio_estacion_coordenadas_N"}))[
                                                           port].get_text(),
                                                       list(soup.find_all(name="span",
                                                                          attrs={
                                                                              "class": "sitio_estacion_coordenadas_W"}))[
                                                           port].get_text()]])
                    else:
                        print("a")
                        port_len = len(soup.find_all(name='a', attrs={"class": "sitio_estacion_a"}))
                        for port in range(0, port_len):
                            port_url = list(soup.find_all(name='a', attrs={"class": "sitio_estacion_a"}))[port]
                            if list(soup.find_all(name='a', attrs={"class": "sitio_estacion_a"}))[port] is not None:
                                print(port_url['href'])
                                print(port_url['href'].split('/')[-1])
                                print(list(soup.find_all(name="span", attrs={"class": "sitio_estacion_coordenadas_N"}))[
                                          port].get_text())
                                print(list(soup.find_all(name="span", attrs={"class": "sitio_estacion_coordenadas_W"}))[
                                          port].get_text())
                                writer.writerows([[port_url['href'].split('/')[-1],
                                                   list(soup.find_all(name="span",
                                                                      attrs={"class": "sitio_estacion_coordenadas_N"}))[
                                                       port].get_text(),
                                                   list(soup.find_all(name="span",
                                                                      attrs={"class": "sitio_estacion_coordenadas_W"}))[
                                                       port].get_text()]])
