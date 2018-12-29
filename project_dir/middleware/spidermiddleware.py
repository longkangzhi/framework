class Spidermiddleware1(object):
    def process_request(self, request):
        print('spidermiddleware1_request{}'.format(request.url))
        return request

    def process_response(self, response):
        print('spidermiddleware1_response{}'.format(response.url))
        return response


class Spidermiddleware2(object):
    def process_request(self, request):
        print('spidermiddleware2_request{}'.format(request.url))
        return request

    def process_response(self, response):
        print('spidermiddleware2_response{}'.format(response.url))
        return response