import bottle
import begin
import mydb
import connectdb
from sqlalchemy.orm import sessionmaker
import sys

engine = connectdb.engine(database="greeting")

Session = sessionmaker(bind=engine)

session = Session()

@bottle.route("/")
def index():
    try:
        greeting = session.query(mydb.hello).first()
        return greeting.value
    except:
        session.rollback()
        return "ACK DATABASE ERROR"


@begin.start
def run(host="0.0.0.0", port=8080):
    bottle.run(host=host, port=port)