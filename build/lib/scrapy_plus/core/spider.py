from ..h_ttp.request import Request
from ..item import Item
class Spider(object):
    name = 'spider'
    # def __init__(self):
    start_urls = []

    def start_request(self):
        for start_url in self.start_urls:
            yield Request(start_url) #使url成为一个对象

    def parse(self, response):
        # print(response.body.decode())
        return Item(response.url)
