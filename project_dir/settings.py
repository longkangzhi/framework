DEFAULT_LOG_FILENAME = 'longkangzhi.log'
SPIDERS = [
    # 'spider.sina.SinaSpider',
    'spider.baidu.BaiduSpider',
    # 'spider.douban.DoubanSpider'

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
ASYNC_TYPE='coroutine'

# SCHEDULER_PERSIST = True