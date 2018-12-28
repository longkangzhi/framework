from .downloader import Download
from .spider import Spider
from .pipeline import Pipeline
from .scheduler import Scheduler
from ..h_ttp.request import Request
from ..middleware.spidermiddleware import Spidermiddleware
from ..middleware.downloadermiddleware import Downloadermiddleware
from ..utilis.log import logger
from datetime import datetime


class Engine(object):

    def __init__(self,spider):
        self.spider = spider
        self.downloader = Download()
        self.pipeline = Pipeline()
        self.scheduler = Scheduler()
        self.downloadermiddleware = Downloadermiddleware()
        self.spidermoddleware = Spidermiddleware()

    def start(self):
        start = datetime.now()
        logger.info('开始时间{}'.format(start))
        self.__start()
        end = datetime.now()
        logger.info('结束时间{}'.format(end))
        logger.info('总耗时{}'.format((end-start).total_seconds()))



    def __start(self):
        for request in self.spider.start_request():
        # request = self.spider.start_request()
            request = self.spidermoddleware.process_request(request)
            self.scheduler.add_request(request)
        request = self.scheduler.get_request()
        request = self.downloadermiddleware.process_request(request)
        response = self.downloader.get_response(request)
        response = self.downloadermiddleware.process_response(response)
        response = self.spidermoddleware.process_response(response)
        result = self.spider.parse(response)
        if isinstance(result, Request):
            result = self.spidermoddleware.process_request(result)
            self.scheduler.add_request(result)

        else:
            self.pipeline.process_item(result, self.spider)












