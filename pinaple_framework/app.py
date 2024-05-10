from webob import Request, Response

from parse import parse


class PineApple:

    def __init__(self):
        self._routes = dict()

    def __call__(self, environ, start_response):
        request = Request(environ=environ)
        response = self.handle_request(request=request)
        return response(environ=environ, start_response=start_response)

    def route(self, path):
        def wrapper(handler):
            self._routes[path] = handler
            return handler

        return wrapper

    def find_handler(self, request):

        for path, handler in self._routes.items():

            parsed_result = parse(format=path, string=request.path)
            if parsed_result:
                return handler, parsed_result.named

        return None, None

    def handle_request(self, request):
        response = Response()

        handler, kwargs = self.find_handler(request)
        handler(request, response, **kwargs) if handler else self.default_response(response)
        return response

    @staticmethod
    def default_response(response):
        response.status_code = 404
        response.text = "404 Page not Found"


class PineAppleFrame(PineApple):
    pass
