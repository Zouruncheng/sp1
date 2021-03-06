

# 自定义命令执行所有爬虫
from scrapy.commands import ScrapyCommand
from scrapy.utils.project import get_project_settings


class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return 'Runs all of the spiders'

    def run(self, args, opts):
        # 获取爬虫列表
        spider_list = self.crawler_process.spiders.list()
        for name in spider_list:
            # 初始化爬虫
            self.crawler_process.crawl(name, **opts.__dict__)
        # 开始执行所有爬虫
        self.crawler_process.start()