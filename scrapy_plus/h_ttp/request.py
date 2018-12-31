class Request(object):
    def __init__(self, url, method='GET', headers={}, params={}, data={}, callback=None, meta={}, dont_filter=None):
        self.url = url
        self.method = method
        self.headers = headers
        self.params = params
        self.data = data
        self.callback = callback
        self.meta = meta
        self.dont_filter = dont_filter
