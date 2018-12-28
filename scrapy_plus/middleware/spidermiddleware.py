class Spidermiddleware(object):
    def process_request(self, request):
        print('spidermiddleware_request{}'.format(request.url))
        return request

    def process_response(self, response):
        print('spidermiddleware_response{}'.format(response.url))
        return response