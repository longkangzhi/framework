from scrapy_plus.core.spider import Spider
from scrapy_plus.h_ttp.request import Request


class DoubanSpider(Spider):
    def start_request(self):
        url_pattern = 'https://movie.douban.com/top250?start={}&filter='
        for i in range(0, 250, 25):
            url = url_pattern.format(i)
            yield Request(url)