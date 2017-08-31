# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request

class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['dig.chouti.com']
    start_urls = ['http://dig.chouti.com/']



    def parse(self, response):
        """回调函数"""
        article_id_list = Selector(response=response).xpath(
            "//div[@class='content-list']//div[@class='item']//div[@class='news-pic']//img[re:test(@lang,'\d+')]/@lang"
        ).extract()
        print(article_id_list) # ['13990746', '13990001', '13986316']

        page_url_list = Selector(response=response).xpath(
            "//div[@id='page-area']//a[re:test(@href,'/all/hot/recent/\d+')]/@href"
        ).extract()
        print(page_url_list)

        # 点赞
        for article_id in article_id_list:
            vote_url="http://dig.chouti.com/link/vote?linksId=%s" % article_id
            yield Request(
                url=vote_url,
                method="post",
                callback=self.parse,
                cookies=

            )







