from pinaple_framework import PineAppleFrame

app = PineAppleFrame()


@app.route(path="/home")
def home(request, response):
    response.text = "Hello from home page"


@app.route(path="/about")
def about(request, response):
    response.text = "Hello from about page"


@app.route(path="/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}!"


@app.route(path="/books")
class Book:

    def get(self, request, response):
        response.text = "Hello from book page"

    def post(self, request, response):
        response.text = "Book created endpoint successfully work."
