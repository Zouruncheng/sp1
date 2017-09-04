# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class Sp1Pipeline(object):
    '''spider每次yield一个Item对象，则会执行一次process_item方法，四个方法都建议写'''
    def __init__(self):
        self.f = None

    def process_item(self, item, spider):
        """
        item：{'link': 'http://jandan.net/2017/08/31/supernatural-radio.html',}
        每个item pipeline组件都需要调用该方法，
        这个方法必须返回一个具有数据的dict，或是 Item (或任何继承类)对象，
        或是抛出 DropItem 异常，被丢弃的item将不会被之后的pipeline组件所处理。
        """
        if spider.name == 'jiadnan':
            pass
        # data = json.dumps(dict(item)) + "\n"
        data = str(item) + "\n"
        self.f.write(data)
        # 将item传递给下一个pipeline的process_item方法
        return item

        # 抛出异常后，下一个pipeline的process_item方法不在执行
        # from scrapy.exceptions import DropItem
        # raise DropItem()  下一个pipeline的process_item方法不在执行

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        # val = crawler.settings.get('MMMM')
        print('执行pipeline的from_crawler，进行实例化对象')
        return cls()

    def open_spider(self,spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        print('打开爬虫')
        self.f = open('jiandan.log', 'a+')

    def close_spider(self,spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        print("关闭爬虫")
        self.f.close()

