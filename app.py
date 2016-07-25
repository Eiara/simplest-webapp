import bottle
import begin

@bottle.route("/")
def index():
	return b"hello"


@begin.start
def run(host="0.0.0.0", port=8080):
    bottle.run(host=host, port=port)