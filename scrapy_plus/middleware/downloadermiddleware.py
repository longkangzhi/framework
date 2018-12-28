class Downloadermiddleware(object):
    def process_request(self, request):
        print('downloadermiddleware_request{}'.format(request.url))
        return request

    def process_response(self, response):
        print('downloadermiddleware_response{}'.format(response.url))
        return response