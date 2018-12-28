from scrapy_plus.core.engine import Engine
from spider.baidu import BaiduSpider



if __name__ == "__main__":
    baidu_spider = BaiduSpider()
    engine = Engine(baidu_spider)
    engine.start()
