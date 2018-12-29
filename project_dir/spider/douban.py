from scrapy_plus.core.spider import Spider
from scrapy_plus.h_ttp.request import Request
from scrapy_plus.item import Item


class DoubanSpider(Spider):
    def start_request(self):
        url_pattern = 'https://movie.douban.com/top250?start={}&filter='
        for i in range(0, 250, 25):
            url = url_pattern.format(i)
            yield Request(url)

    def parse(self, response):
        a_s = response.xpath('//div[@class="hd"]/a')
        for a in a_s:
            data ={}
            data['moovie_url'] = a.xpath('./span[1]/text()')[0]
            data['movie_url'] = a.xpath('./@href')[0]
            yield Item(data)


        # return Item(response.url)