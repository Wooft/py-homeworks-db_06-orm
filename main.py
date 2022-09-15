import json
import os
import pathlib
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from base import create_tables, Book, Publisher, Shop, Stock, Sale

def CreateEngine():
    DSN = 'postgresql://postgres:Shambala@localhost:5432/db06'
    engine = sqlalchemy.create_engine(DSN)
    return (engine)

def GetData():
    path = os.path.join(pathlib.Path.cwd(), "tests_data.json")
    with open(path, 'r') as file:
        data = json.load(file)
    return data

def CreateTables(engine):
    create_tables(engine)


def PasteData(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    for elements in GetData():
        if elements['model'] == 'publisher':
            pub = Publisher(name=elements['fields']['name'])
            session.add(pub)
        session.commit()
        if elements['model'] == 'book':
            book = Book(title=elements['fields']['title'], id_publisher=elements['fields']['id_publisher'])
            session.add(book)
        session.commit()
        if elements['model'] == 'shop':
            shop = Shop(name=elements['fields']['name'])
            session.add(shop)
        session.commit()
        if elements['model'] == 'stock':
            stock = Stock(id_book=elements['fields']['id_book'], id_shop=elements['fields']['id_shop'],
                          count=elements['fields']['count'])
            session.add(stock)
            session.commit()
        if elements['model'] == 'sale':
            sale = Sale(price=elements['fields']['price'], data_sale=elements['fields']['date_sale'],
                        id_stock=elements['fields']['id_stock'], count=elements['fields']['count'])
            session.add(sale)

    session.commit()
    session.close

def OutDate(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    print('Список издателей: ')
    for c in session.query(Publisher).all():
        print(c)

    print('Список книг: ')
    for c in session.query(Book).all():
        print(c)

    print('Список магазинов: ')
    for c in session.query(Shop).all():
        print(c)

    print('Список наличия: ')
    for c in session.query(Stock).all():
        print(c)

    print('Список скидок: ')
    for c in session.query(Sale).all():
        print(c)

    id = int(input('Enter publisher id: '))
    for c in session.query(Publisher).filter(Publisher.id == id).all():
        print(c)
    session.close()


if __name__ == "__main__":
    CreateTables(CreateEngine())
    PasteData(CreateEngine())
    OutDate(CreateEngine())


