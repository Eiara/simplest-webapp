import connectdb
import mydb
from sqlalchemy.orm import sessionmaker

def create_database(engine):
    engine.execute("CREATE DATABASE greeting;")

def init(engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    mydb.Base.metadata.create_all(engine)
    row = mydb.hello(value="database hello", id=1)

    session.add(row)
    session.commit()