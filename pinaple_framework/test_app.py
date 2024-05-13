import pytest


def test_basic_route_adding(app):
    @app.route(path="/home")
    def home(request, response):
        response.text = "Hello from home page"


def test_duplicate_routes_throws_exception(app):
    @app.route(path="/home")
    def home(request, response):
        response.text = "Hello from home page"

    with pytest.raises(AssertionError):
        @app.route(path="/home")
        def home2(request, response):
            response.text = "Hello from home2 page"


def test_requests_can_be_sent_by_test_client(app, test_client):
    @app.route(path="/home")
    def home(request, response):
        response.text = "Hello from home page"

    resp = test_client.get(url="http://testserver/home")

    assert resp.status_code == 200
    assert resp.text == "Hello from home page"


def test_parameterized_routing(app, test_client):
    @app.route(path="/hello/{name}")
    def greeting(request, response, name):
        response.text = f"Hello, {name}!"

    resp = test_client.get(url="http://testserver/hello/pineapple-framework")

    assert resp.status_code == 200
    assert resp.text == "Hello, pineapple-framework!"


def test_default_response(test_client):
    assert test_client.get(url="http://testserver/hello/pineapple-framework").status_code == 404
    assert test_client.get(url="http://testserver/hello/akuna-matata").text == "404 Page not Found"


def test_class_based_handler(app, test_client):
    @app.route(path="/examples")
    class ExampleHandler:
        def get(self, request, response):
            response.status = 200
            response.text = "This is a class based handler for the 'get' method"

        def post(self, request, response):
            response.text = "This is a class based handler for the 'post' method"

    resp = test_client.get(url="http://testserver/examples")
    assert resp.status_code == 200
    assert resp.text == "This is a class based handler for the 'get' method"

    resp = test_client.post(url="http://testserver/examples")
    assert resp.status_code == 200
    assert resp.text == "This is a class based handler for the 'post' method"

    resp = test_client.patch(url="http://testserver/examples")
    assert resp.status_code == 405
    assert resp.text == "Method not allowed"
