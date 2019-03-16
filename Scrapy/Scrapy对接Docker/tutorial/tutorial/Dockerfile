FROM python:3.7
ENV PATH C:\Users\thinkpad\Desktop\Python\Python入门练兵场\Scrapy框架的使用\Scrapy对接Docker\tutorial\tutorial:$PATH
ADD .  /code
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD scrapy crawl quotes