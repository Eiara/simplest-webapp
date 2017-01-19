import bottle
import begin
import os

@bottle.route("/")
def index():
    return b"hello"


@begin.start
def run(host="0.0.0.0", port=8080):
    if os.environ.get("APP_PORT"):
        port = int(os.environ.get("APP_PORT"))
    bottle.run(host=host, port=port)