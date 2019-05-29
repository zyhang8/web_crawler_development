# -*- coding: utf-8 -*-
import scrapy
# 导入数据结构类
from huaproject.items import HuaprojectItem


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['www.xiaohuar.com']
    # 基础url
    url = 'http://www.xiaohuar.com/list-1-'
    # 爬取的起始页
    page = 0
    # 爬取的起始url
    start_urls = ['http://www.xiaohuar.com/hua/list-1-0.html']

    # 定义的方法，注意这个方法名不能修改，传入的参数也不能修改，否则会出错
    def parse(self, response):
        # print(100)
        # 解析所有校花，获取指定内容
        div_list = response.xpath('//div[@class="item masonry_brick"]')
        # print(div_list)
        # 遍历上面所有的div，找到指定的内容即可
        for div in div_list:
            # 创建item对象 就是我们在items里面定义的类
            item = HuaprojectItem()
            image_url = div.xpath('./div[@class="item_t"]/div[@class="img"]/a/img/@src').extract_first()
            # 处理周半仙图片是以.php结尾的
            if image_url.endswith('.php'):
                image_url = image_url.replace('.php', '.jpg')

            # 拼接图片的全路径
            image_url = 'http://www.xiaohuar.com' + image_url

            name = div.xpath('./div[@class="item_t"]/div[@class="img"]/span[@class="price"]/text()').extract_first()
            school = div.xpath('./div[@class="item_t"]/div[@class="img"]/div[@class="btns"]/a/text()').extract_first()
            like = div.xpath('./div[contains(@class,"item_b")]//em[@class="bold"]/text()').extract_first()
            # 将上面提取的属性保存到对象中
            item['image_url'] = image_url
            item['name'] = name
            item['school'] = school
            item['like'] = like
            # 将该item对象返回
            yield item

        # url = 'http://www.xiaohuar.com/hua/list-1-'
        # page = 0
        # 当处理完第一页的时候，要接着发送请求，处理下一页
        self.page += 1
        if self.page <= 11:
            url = self.url + str(self.page) + '.html'
            # 再次的发送请求，并且指定回调处理函数进行处理对应的请求
            yield scrapy.Request(url=url, callback=self.parse)
