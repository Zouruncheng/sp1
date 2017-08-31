import scrapy
from scrapy.selector import Selector
from scrapy.http import Request


class JiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/']

    def parse(self, response):
        hxs = Selector(response=response).xpath("//div[@id='content']")
        hxs1 = hxs.xpath(".//div[@class='indexs']/h2/a").extract()
        print(hxs1)
        # for item in hxs1:
        #     with open("imgs", "wb") as f:
        #         f.write(item.body)

        # 获取页码a标签
        result = hxs.xpath(".//div[@class='wp-pagenavi']/a[re:test(@href,'http://jandan.net/page/\d+')]/@href").extract()
        # // *[ @ id = "content"]/ div[28] / a[1]

        for url in result:
            print(url)
            yield Request(url=url, callback=self.parse)











