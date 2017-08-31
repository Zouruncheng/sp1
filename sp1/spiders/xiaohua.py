# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://xiaohuar.com/']

    def parse(self, response):
        hxs = Selector(response=response)

