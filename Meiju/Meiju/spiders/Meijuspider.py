# -*- coding: utf-8 -*-
import scrapy

# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from Meiju.items import MeijuItem


# from .Meiju.pipelines import MeijuPipeline

class MeijuspiderSpider(scrapy.Spider):
    name = 'Meijuspider'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://meijutt.com/new100.html']

    def parse(self, response):
        # print(response.body)
        content = etree.HTML(response.body.decode('GBK'))
        movies = content.xpath('//ul[@class="top-list  fn-clear"]/li')
        for movie in movies:
            # print(movie)
            # 美剧名
            a_list = movie.xpath('./h5/a')
            a = a_list[0].text
            # 美剧更新状态
            stars = movie.xpath('.//span[@class="state1 new100state1"]/font')[0].text
            # print(a,stars)

            item = MeijuItem()
            item['name'] = a
            item['state'] = stars
            print(a, '-----', stars)

            # 使用yield返回数据
            yield item
