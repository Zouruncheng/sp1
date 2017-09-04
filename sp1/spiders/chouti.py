# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request


class ChoutiSpider(scrapy.Spider):
    '''
    登录抽屉并循环点赞
    '''
    name = 'chouti'
    allowed_domains = ['dig.chouti.com']
    start_urls = ['http://dig.chouti.com/']
    cookie_dict = {}

    def start_requests(self):
        """重写start_requests()方法，进入爬虫。指定callback，登录抽屉"""
        print("1.start craw")

        for url in self.start_urls:
            yield Request(url, dont_filter=True, callback=self.parse1)

    def parse1(self, response):
        """1.获取首页的cookies。2.携带cookies登录"""
        from scrapy.http.cookies import CookieJar
        cookies_jar = CookieJar()  # cookies_jar对象，封装了 cookies
        cookies_jar.extract_cookies(response, response.request)  # 提取cookies
        # self.cookies_jar = cookies_jar

        # 获取cookies字典
        for k, v in cookies_jar._cookies.items():
            for i, j in v.items():
                for m, n in j.items():
                    self.cookie_dict[m] = n.value
        print("2.get cookies dict")
        print(self.cookie_dict)

        url = "http://dig.chouti.com/login"
        yield Request(
            url=url,
            method="POST",
            headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},
            body="phone=8618071540800&password=249907348&oneMonth=1",  # 用户名和密码
            cookies=self.cookie_dict,
            callback=self.vote_index,
        )

    def vote_index(self, response):
        """登录后进入首页。"""
        print("3.login successful")
        print(response.text)
        yield Request(
            url="http://dig.chouti.com",
            method="GET",
            cookies=self.cookie_dict,
            # dont_filter=True,
            callback=self.show,
        )


    def show(self, response):
        """回调函数"""
        print("4.start vote")
        article_id_list = Selector(response=response).xpath(
            "//div[@class='content-list']//div[@class='item']//div[@class='news-pic']//img[re:test(@lang,'\d+')]/@lang"
        ).extract()
        # print(article_id_list) # ['13990746', '13990001', '13986316']


        # TODO:取消点赞http://dig.chouti.com/vote/cancel/vote.do
        # 点赞
        for article_id in article_id_list:
            vote_url = "http://dig.chouti.com/link/vote?linksId=%s" % (article_id,)
            yield Request(
                url=vote_url,
                method="POST",
                callback=self.lastt,
                cookies=self.cookie_dict,
            )

        # 翻页
        page_url_list = Selector(response=response).xpath(
            "//div[@id='page-area']//a[re:test(@href,'/all/hot/recent/\d+')]/@href"
        ).extract()
        for url in page_url_list:
            yield Request(
                url="http://dig.chouti.com"+url,
                method="GET",
                callback=self.show
            )

    def lastt(self, response):
        print(response.text)
