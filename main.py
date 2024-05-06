from wsgiref.simple_server import make_server


# https://peps.python.org/pep-0333/
def sample_app(environ, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]

    start_response(status, headers)
    return [b"Hello World"]


server = make_server(
    host="localhost",
    port=8080,
    app=sample_app
)
server.serve_forever()
