from ..h_ttp.request import Request
from ..item import Item
class spider(object):
    # def __init__(self):
    start_url = 'http://www.itcast.cn'

    def start_request(self):
        return Request(self.start_url) #使url成为一个对象

    def parse(self, response):
        print(response.text)
        return Item(response.url)