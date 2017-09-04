from scrapy import signals


class MyExtension(object):
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_crawler(cls, crawler):
        val = crawler.settings.getint('MMMM')
        ext = cls(val)

        # 在scrapy中注册信号： spider_opened,信号触发后执行ext.opened函数
        crawler.signals.connect(ext.opened, signal=signals.spider_opened)
        # 在scrapy中注册信号： spider_closed
        crawler.signals.connect(ext.closed, signal=signals.spider_closed)

        return ext
    def opened(self, spider):
        print('自定义扩展:open')

    def closed(self, spider):
        print('自定义扩展:close')