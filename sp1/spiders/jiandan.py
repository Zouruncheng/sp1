import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.dupefilters import RFPDupeFilter


class JiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/']

    def parse(self, response):
        """爬煎蛋首页文章标题和链接，用pipeline写入文本，"""
        print("爬煎蛋")
        # 获取文章标题
        hxs = Selector(response=response).xpath("//div[@id='content']")
        tag_list = hxs.xpath(".//div[@class='indexs']/h2/a")
        for tag in tag_list:
            # title = tag.xpath("./text()").extract()        # 获取的是列表
            title = tag.xpath("./text()").extract_first()  # 获取的是字符串
            link = tag.xpath("./@href").extract_first()
            from ..items import Sp1Item
            yield Sp1Item(title=title, link=link)


        # title_list = hxs.xpath(".//div[@class='indexs']/h2/a/text()").extract()
        # print(title_list)

        # 获取a标签
        # link_list = hxs.xpath(".//div[@class='indexs']/h2/a/@href").extract()
        # print(link_list)













