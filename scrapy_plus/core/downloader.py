import requests
from ..h_ttp.response import Response


class Download(object):
    def get_response(self, request):
        if request.method.lower() == 'get':
            resp = requests.get(request.url, headers=request.headers, params=request.params)
        elif request.method.lower() == 'post':
            resp = requests.post(request.url, headers=request.headers, data=request.data)
        else:
            raise Exception('暂时只支持GET 和 POST请求')

        return Response(resp.url, status_code=resp.status_code, headers=resp.headers, body=resp.content)

