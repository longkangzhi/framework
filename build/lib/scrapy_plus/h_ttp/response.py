class Response(object):
    def __init__(self, url, status_code=200, headers={}, body=None):
        self.url = url
        self.status_code = status_code
        self.headers = headers
        self.body = body
