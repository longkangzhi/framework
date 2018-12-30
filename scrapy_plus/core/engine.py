

import importlib

from scrapy_plus.conf import settings
if settings.ASYNC_TYPE.lower() == 'thread':
   from multiprocessing.dummy import Pool
else:
    from ..asyn.coroutine import Pool
from .downloader import Download
from collections import Iterable
from .spider import Spider
from .pipeline import Pipeline
from .scheduler import Scheduler
from ..h_ttp.request import Request
from ..middleware.spidermiddleware import Spidermiddleware
from ..middleware.downloadermiddleware import Downloadermiddleware
from ..utilis.log import logger
import time
from datetime import datetime



class Engine(object):

    # def __init__(self, spiders, pipelines, downloadmiddlewares,spidermiddlewares ):
    #     self.spiders = spiders
    #     self.downloader = Download()
    #     self.pipelines = pipelines
    #     self.scheduler = Scheduler()
    #     self.downloadermiddlewares = downloadmiddlewares
    #     self.spidermiddlewares= spidermiddlewares
    #     # self.callback = Request.callback
    #     self.total_response_nums = 0

    def __init__(self):
        self.spiders = self.__auto_import(settings.SPIDERS, isSpider=True)
        self.downloader = Download()
        self.pipelines = self.__auto_import(settings.PIPELINES)
        self.scheduler = Scheduler()
        self.downloadermiddlewares = self.__auto_import(settings.DOWNLOADER_MIDDLERWARE)
        self.spidermiddlewares = self.__auto_import(settings.SPIDER_MIDDLEWARE)
        # self.callback = Request.callback
        self.pool = Pool()
        self.total_response_nums = 0


    def __auto_import(self,full_names, isSpider=False):
        results = {} if isSpider else []
        for full_name in full_names:
            module_name, class_name = full_name.rsplit('.', maxsplit=1)
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name)
            instance = cls()
            if isSpider:
                results[instance.name] = instance
            else:
                results.append(instance)
        return results





    def start(self):
        start = datetime.now()
        logger.info('开始时间{}'.format(start))
        logger.info('爬虫 {}'.format(settings.SPIDERS))
        logger.info('管道 {}'.format(settings.PIPELINES))
        logger.info('下载中间件 {}'.format(settings.DOWNLOADER_MIDDLERWARE))
        logger.info('爬虫中间件 {}'.format(settings.SPIDER_MIDDLEWARE))
        self.__start()
        end = datetime.now()
        logger.info('结束时间{}'.format(end))
        logger.info('总耗时{}'.format((end-start).total_seconds()))
        logger.info('入队数量 {}'.format(self.scheduler.total_request_nums))
        logger.info('过滤数量 {}'.format(self.scheduler.filter_request_nums))
        logger.info('响应数量 {}'.format(self.total_response_nums))

    def __error_callback(self, ex):
        try:
            raise ex
        except Exception as e :
            logger.exception(e)

    def __execute_callback(self, item):
        self.pool.apply_async(self.__execute_request_response_item, callback=self.__execute_callback, error_callback=self.__error_callback )

    def __start(self):
        self.pool.apply_async(self.__add_start_requests, error_callback=self.__error_callback)
        # self.__add_start_requests()
        for i in range (settings.ASYNC_COUNT):
            self.pool.apply_async(self.__execute_request_response_item, callback=self.__execute_callback, error_callback=self.__error_callback)
        time.sleep(0.1)
        while True:
            # self.__execute_request_response_item()
            time.sleep(0.1)
            if self.total_response_nums >= self.scheduler.total_request_nums:
                break

    def __execute_request_response_item(self):
        # self.__add_start_requests()
        # 1/0
        request = self.scheduler.get_request()
        spider = self.spiders[request.spider_name]
        for downloadermiddleware in self.downloadermiddlewares:
            request = downloadermiddleware.process_request(request)
        response = self.downloader.get_response(request)
        response.meta = request.meta
        for downloadermiddleware in self.downloadermiddlewares:
            response = downloadermiddleware.process_response(response)
        for spidermiddleware in self.spidermiddlewares:
            response = spidermiddleware.process_response(response)
        if request.callback:
            results = request.callback(response)
        else:
            results = spider.parse(response)
        if not isinstance(results, Iterable):
            results = [results]
        for result in results:

            if isinstance(result, Request):
                for spidermiddleware in self.spidermiddlewares:
                    result = spidermiddleware.process_request(result)
                result.spider_name = spider.name
                self.scheduler.add_request(result)

            else:
                for pipeline in self.pipelines:
                    result = pipeline.process_item(result, spider)#result = Item(data)

        self.total_response_nums += 1

    def __add_start_requests(self):
        for spider_name, spider in self.spiders.items():
            for request in spider.start_request():
                request.spider_name = spider_name
                # request = self.spider.start_request()
                for spidermiddleware in self.spidermiddlewares:
                    request = spidermiddleware.process_request(request)
                self.scheduler.add_request(request)












