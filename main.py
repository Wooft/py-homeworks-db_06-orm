import sqlalchemy
from sqlalchemy.orm import sessionmaker
from base import create_tables

DSN = 'postgresql://postgres:Shambala@localhost:5432/db06'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)

session = Session()

session.close()