import sqlalchemy
from sqlalchemy.orm import sessionmaker
from base import create_tables, Book, Publisher, Shop, Stock, Sale

DSN = 'postgresql://postgres:Shambala@localhost:5432/db06'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

pub1 = Publisher(name='Первый')
pub2 = Publisher(name='Второй')
session.add_all([pub1, pub2])
session.commit()

id = int(input('Введите id издателя: '))
for c in session.query(Publisher).filter(Publisher.id == id).all():
    print(c)

session.close()