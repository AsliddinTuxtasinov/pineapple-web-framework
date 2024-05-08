from pinaple_framework import PineAppleFrame

app = PineAppleFrame()


@app.route(path="/home")
def home(request, response):
    response.text = "Hello from home page"


@app.route(path="/about")
def about(request, response):
    response.text = "Hello from about page"
