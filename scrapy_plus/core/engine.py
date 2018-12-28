from .downloader import Download
from .spider import Spider
from .pipeline import Pipeline
from .scheduler import Scheduler
from ..h_ttp.request import Request


class Engine(object):

    def __init__(self):
        self.spider = Spider()
        self.downloader = Download()
        self.pipeline = Pipeline()
        self.scheduler = Scheduler()

    def start(self):
        return self.__start()

    def __start(self):
        request = self.spider.start_request()
        self.scheduler.add_request(request)
        request = self.scheduler.get_request()
        response = self.downloader.get_response(request)
        result = self.spider.parse(response)
        if isinstance(request, Request):
            self.scheduler.add_request(result)

        else:
            self.pipeline.process_item(result, self.spider)












