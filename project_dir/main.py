from pipelines import BaiduPipeline, DoubanPipeline, BaiduPipeline2
from scrapy_plus.core.engine import Engine
from spider.baidu import BaiduSpider
from spider.douban import DoubanSpider

if __name__ == "__main__":
    baidu_spider = BaiduSpider()
    douban_spider = DoubanSpider()
    spiders = {
        BaiduSpider.name: baidu_spider,
        DoubanSpider.name: douban_spider
    }
    pipelines = [
        BaiduPipeline(),
        BaiduPipeline2(),
        DoubanPipeline()
    ]
    engine = Engine(spiders, pipelines)
    engine.start()
