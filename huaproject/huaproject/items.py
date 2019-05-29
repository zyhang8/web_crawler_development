# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuaprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 需要的数据现在这里制定好，因为在settings里面已近设置好了，所以可以和pipelines联系在一块处理数据
    # 图片链接
    image_url = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 大学
    school = scrapy.Field()
    # 喜欢数
    like = scrapy.Field()
