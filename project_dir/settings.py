DEFAULT_LOG_FILENAME = 'longkangzhi.log'
SPIDERS = [
    'spider.baidu.BaiduSpider',
    # 'spider.douban.DoubanSpider'
    'spider.sina.SinaSpider'
]

PIPELINES = [
    'pipelines.BaiduPipeline',
    # 'pipelines.BaiduPipeline2',
    'pipelines.DoubanPipeline'
]

# DOWNLOADER_MIDDLERWARE = [
#     'middleware.downloadermiddleware.Downloadermiddleware1',
#     'middleware.downloadermiddleware.Downloadermiddleware2'
# ]
#
# SPIDER_MIDDLEWARE =[
#     'middleware.spidermiddleware.Spidermiddleware1',
#     'middleware.spidermiddleware.Spidermiddleware2'
# ]
ASYNC_TYPE='123'

SCHEDULER_PERSIST = True