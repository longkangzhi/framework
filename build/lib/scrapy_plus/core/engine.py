from .downloader import Download
from collections import  Iterable
from .spider import Spider
from .pipeline import Pipeline
from .scheduler import Scheduler
from ..h_ttp.request import Request
from ..middleware.spidermiddleware import Spidermiddleware
from ..middleware.downloadermiddleware import Downloadermiddleware
from ..utilis.log import logger
from datetime import datetime


class Engine(object):

    def __init__(self, spiders, pipelines):
        self.spiders = spiders
        self.downloader = Download()
        self.pipelines = pipelines
        self.scheduler = Scheduler()
        self.downloadermiddleware = Downloadermiddleware()
        self.spidermoddleware = Spidermiddleware()
        # self.callback = Request.callback
        self.total_response_nums = 0

    def start(self):
        start = datetime.now()
        logger.info('开始时间{}'.format(start))
        self.__start()
        end = datetime.now()
        logger.info('结束时间{}'.format(end))
        logger.info('总耗时{}'.format((end-start).total_seconds()))



    def __start(self):
        self.__add_start_requests()
        while True:
            self.__execute_request_response_item()
            if self.total_response_nums >= self.scheduler.total_request_nums:
                break

    def __execute_request_response_item(self):
        # self.__add_start_requests()
        request = self.scheduler.get_request()
        spider = self.spiders[request.spider_name]
        request = self.downloadermiddleware.process_request(request)
        response = self.downloader.get_response(request)
        response.meta = request.meta
        response = self.downloadermiddleware.process_response(response)
        response = self.spidermoddleware.process_response(response)
        if request.callback:
            results = request.callback(response)
        else:
            results = spider.parse(response)
        if not isinstance(results, Iterable):
            results = [results]
        for result in results:

            if isinstance(result, Request):
                result = self.spidermoddleware.process_request(result)
                result.spider_name = spider.name
                self.scheduler.add_request(result)

            else:
                for pipeline in self.pipelines:
                    result = pipeline.process_item(result, spider)

        self.total_response_nums += 1

    def __add_start_requests(self):
        for spider_name, spider in self.spiders.items():
            for request in spider.start_request():
                request.spider_name = spider_name
                # request = self.spider.start_request()
                request = self.spidermoddleware.process_request(request)
                self.scheduler.add_request(request)












