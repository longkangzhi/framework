from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool as BasePool

class Pool(BasePool):
    def apply_async(self, func, args=(), kwds={}, callback=None,error_callback=None):
        super().apply_async(func, args=args, kwds=kwds, callback=callback)

    def closs(self):
        pass