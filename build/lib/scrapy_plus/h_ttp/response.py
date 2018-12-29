import json
import re

from lxml import etree

class Response(object):
    def __init__(self, url, status_code=200, headers={}, body=None, meta={}):
        self.url = url
        self.status_code = status_code
        self.headers = headers
        self.body = body
        self.meta = meta

    def xpath(self, path):
        element = etree.HTML(self.body)
        return element.xpath(path)


    def json(self):
        return json.loads(self.body.decode())

    def find_all(self, pattern, content=None):
        if content is None:
            content = re.findall(pattern, self.body)
            return content
        else:
            return re.findall(pattern, content)


