import bottle
import begin
import mydb
import connectdb
from sqlalchemy.orm import sessionmaker

engine = connectdb.create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)

session = Session()

@bottle.route("/")
def index():
    greeting = session.query(mydb.hello).first()
    return greeting.value


@begin.start
def run(host="0.0.0.0", port=8080):
    bottle.run(host=host, port=port)