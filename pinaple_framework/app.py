import inspect

import requests
import wsgiadapter
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
        assert path not in self._routes, f"Route '{path}' already exists, Duplicate route. Please change it."

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

    def handle_request(self, request, response=Response()):
        handler, kwargs = self.find_handler(request)

        if not handler:
            self.default_response(response)
            return response

        if not inspect.isclass(handler):
            handler(request, response, **kwargs)
            return response

        handler = getattr(handler, request.method.lower(), None)
        if handler is None:
            self.default_response(response, status_code=405, text="Method not allowed")
            return response

        handler(handler, request, response, **kwargs)
        return response

    @staticmethod
    def default_response(response, status_code=404, text="404 Page not Found"):
        response.status_code = status_code
        response.text = text


class PineAppleFrame(PineApple):
    def test_session(self):
        session = requests.Session()
        session.mount('http://testserver', wsgiadapter.WSGIAdapter(self))
        return session
