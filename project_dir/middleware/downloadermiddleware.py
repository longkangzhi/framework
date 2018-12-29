class Downloadermiddleware1(object):
    def process_request(self, request):
        print('downloadermiddleware1_request{}'.format(request.url))
        return request

    def process_response(self, response):
        print('downloadermiddleware1_response{}'.format(response.url))
        return response


class Downloadermiddleware2(object):
    def process_request(self, request):
        print('downloadermiddleware2_request{}'.format(request.url))
        return request

    def process_response(self, response):
        print('downloadermiddleware2_response{}'.format(response.url))
        return response