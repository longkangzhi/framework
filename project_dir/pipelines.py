from spider.baidu import BaiduSpider
from spider.douban import DoubanSpider


class BaiduPipeline(object):
    def process_item(self, item, spider):
        # print(spider.name)
        if spider.name == BaiduSpider.name:
            print('百度管道1: {}'.format(item.data))
        print(item)
        return item
class BaiduPipeline2(object):
    def process_item(self, item, spider):
        if spider.name == BaiduSpider.name:
            print('百度管道2: {}'.format(item.data))
        return item


class DoubanPipeline(object):
    def process_item(self, item, spider):
        if spider.name == DoubanSpider.name:
            print(spider.name)
            print(DoubanSpider.name)
            print(item)
            print('豆瓣管道: {}'.format(item.data))
        return item