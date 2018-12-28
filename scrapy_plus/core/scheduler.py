from queue import Queue

class Scheduler(object):
    def __init__(self):
        self.queue = Queue()

    def add_request(self, request):
        return self.queue.put(request)

    def get_request(self):
        return self.queue.get()

    def reques_seen(self, request):
        pass
