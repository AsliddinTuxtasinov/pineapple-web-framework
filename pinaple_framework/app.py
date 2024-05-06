from webob import Request, Response


class PineAppleFrame:

    # def __call__(self, environ, start_response):
    #     status = "200 OK"
    #     headers = [("Content-Type", "text/plain")]
    #
    #     start_response(status, headers)
    #     return [b"Hello World"]

    # https://docs.pylonsproject.org/projects/webob/en/stable/reference.html#request
    def __call__(self, environ, start_response):
        request = Request(environ=environ)

        # response = Response()
        # response.text = "'Hello World' from pineapple web framework !!!"

        response = self.handle_request(request=request)
        return response(environ=environ, start_response=start_response)

    @staticmethod
    def handle_request(request):
        user_agent = request.environ.get('HTTP_USER_AGENT', "User Agent not Found")

        response = Response()
        response.text = f"Hello World with user agent: {user_agent}"
        return response
