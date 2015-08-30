import bottle
import begin
import socket

fqdn = socket.gethostname()

@bottle.route("/")
def index():
	return fqdn + "\n"


@begin.start
def run(host="0.0.0.0", port=9080):
    bottle.run(host=host, port=port)