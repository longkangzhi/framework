from scrapy_plus.core.engine import Engine
from spider.baidu import BaiduSpider
from spider.douban import DoubanSpider

if __name__ == "__main__":
    baidu_spider = BaiduSpider()
    douban_spider = DoubanSpider()
    engine = Engine(douban_spider)
    engine.start()
