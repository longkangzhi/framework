import hashlib

import six
from scrapy_plus.conf import settings
# from six.moves.queue import Queue
from w3lib.url import canonicalize_url

from scrapy_plus.utilis.log import logger
if settings.SCHEDULER_PERSIST:
    from scrapy_plus.utilis.queue import Queue
    from scrapy_plus.utilis.set import RedisFilterContainer as FilterContainer
else:
    from six.moves.queue import Queue
    from scrapy_plus.utilis.set import NoramlFilterContainer as FilterContainer

class Scheduler(object):
    def __init__(self, stats_collector):
        self.queue = Queue()

        self.filter_containers = FilterContainer()
        # self.filter_containerss = set()
        # self.total_request_nums = 0
        # self.filter_request_nums = 0
        self.states_collector = stats_collector
    def add_request(self, request):
        if self.reques_seen(request):
            logger.info('被过滤掉的请qiu {}'.format(request.url))
            # self.filter_request_nums += 1
            self.states_collector.incr(self.states_collector.repeat_request_nums_key)

            return
        self.queue.put(request)
        # self.total_request_nums += 1
        self.states_collector.incr(self.states_collector.request_nums_key)

    def get_request(self):
        return self.queue.get()

    def reques_seen(self, request):
        fp = self.gen_fp(request)
        # if fp in self.filter_containers:
        if self.filter_containers.exists(fp):
            return True
        self.filter_containers.add_fp(fp)
        return False


    def gen_fp(self, request):
        url = canonicalize_url(request.url)
        method = request.method.upper()
        params = sorted(request.params.items(), key=lambda x: x[0])
        data = sorted(request.data.items(), key=lambda x: x[0])

        sha1 = hashlib.sha1()
        sha1.update(self.str_to_bytes(url))
        sha1.update(self.str_to_bytes(method))
        sha1.update(self.str_to_bytes(str(params)))
        sha1.update(self.str_to_bytes(str(data)))
        return sha1.hexdigest()
    def str_to_bytes(self, s):
        if six.PY3:
            return s.encode('utf-8') if isinstance(s, str) else s

        else:
            return s if isinstance(s, str) else s.encode('utf-8')