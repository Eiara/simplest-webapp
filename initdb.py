import connectdb
import mydb
from sqlalchemy.orm import sessionmaker

engine = connectdb.engine()
Session = sessionmaker(bind=engine)

session = Session()

mydb.Base.metadata.create_all(engine)
row = mydb.hello(value="database hello", id=1)

session.add(row)
session.commit()