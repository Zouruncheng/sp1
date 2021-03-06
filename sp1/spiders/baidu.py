# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/'] # 起始URL

    def parse(self, response):   # 回调函数
        print("开始爬百度")
        # print(response.text)





'''
目录结构
—Project
    |---scrapy.cfg ()   ---项目的主配置信息，爬虫配置在settings.py
    |
    |---Project
           |--__init__.py
           |--items.py        -- 数据存储模板，用于结构化数据。如Django的Model
           |--middlewares.py  -- 
           |--pipelines.py    -- 数据处理行为
           |--settings.py     -- 配置文件
           |
           |--spiders         -- 爬虫目录
                 |---__init__.py
                 |---爬虫1.py
                 |---爬虫2.py
                 
                 
2.选择器
    /@href   # 取属性
    /@text() # 取内容
'''