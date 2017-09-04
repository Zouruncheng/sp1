0.5.spider文件目录
    - baidu 最简单
    - chouti 登录抽屉，携带cookies，循环点赞页面
    - jiandan 爬取文件标题和超链接，pipeline输出到文件


1.起始URL
    - 起始url会封装成Request对象，

2.POST请求头
    cookies = {} or cookiejar对象
    - import urllib.parse
        data = urllib.parse.urlencode({"k1":"v1", "k2":"v2"})
        'k1=v1&k2=v2'


    - cookies
        from scrapy.http.cookies import CookieJar
        cookies_jar = CookieJar()  # cookies_jar对象，封装了 cookies
        cookies_jar.extract_cookies(response, response.request)  # 提取cookies对象

        # 获取cookies字典
        for k, v in cookies_jar._cookies.items():
            for i, j in v.items():
                for m, n in j.items():
                    self.cookie_dict[m] = n.value


3.持久化pipeline和item
    - 在spider中返回一个Item对象
    - 并在settings中注册
    - 爬虫的主要目的就是从web中解析出结构化的数据，Item对象是一个容器，保存了我们爬取到的数据。
    - Item对象收集完数据后，它将会被传递到Item Pipeline，一些组件会按照一定的顺序执行对Item的处理。
    - pipeline的主要作用有
        - 清理HTML数据
        - 验证爬取的数据(检查item包含某些字段)
        - 查重(并丢弃)
        - 将爬取结果保存到数据库中

4.自定义去重规则
    - 1.在settings文件中指定
        DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter'
        DUPEFILTER_DEBUG = False
        JOBDIR = "保存范文记录的日志路径，如：/root/"  # 最终路径为 /root/requests.seen
    - 2.自定义类


5.中间件
    - 下载中间件
        - 1.在settings注册
            - DOWNLOADER_MIDDLEWARES  =  {'sp1.middlewares.DownMiddleware1' :543}
        - "middlewares/DownMiddleware1"
    - 爬虫中间件
        - 配置 + 类

6.自定义扩展
    - 在settings注册
        - EXTENSIONS = {'sp1.extends.MyExtension': 500,}
    - 自定义类
        - "extends/MyExtension"


7.其他
    - scrapy配置文件
        - 代理
            - 1.使用默认的代理
                {http_proxy:http://root:wodetian@192.168.11.11:9999/}
            - 1.自定义下载中间件设置代理 os.environ

        - https证书
            - 1.网站使用可信任的证书
            - 2.网站使用自定义证书
        - 重要
            - 爬虫的名字，和爬虫协议
            - 默认请求头
            - 限速
            - 代理 ***
            - https

8.自定义命令（看源码的入口）
    - 1.在settings中配置
        - COMMANDS_MODULE = 'sp1.commands'

    - 2.定制命令让所有的爬虫开始工作
        - commands/crwalall


9.总结
    - 基础:
        - 起始url(start_request)
        - parse
            - 选择器，
            - yield Item()
            - yield Request()

        - Item()和pipeline()

    - 进阶
        - 去重规则
        - 自定义扩展
        - 中间件
        - 自定义命令
        - 自定制调度器 ***

10.TinyScrapy框架
    - TODO

























