import json


import sqlalchemy
from sqlalchemy.orm import sessionmaker

from classes import create_tables, Publisher, Book, Shop, Stock, Sale

pwd = ''

DSN = f'postgresql://postgres:{pwd}@localhost:5432/netology-orm'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


def open_json():
    with open('test_data.json', 'r') as td:
        data = json.load(td)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]

        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()

# def searching(publisher_id):
    # publisher_subquery = session.query(Publisher).filter(Publisher.name.like(publisher_id)).subquery()
    # book_subquery = session.query(Book).join(publisher_subquery, Book.id == publisher_subquery.c.id)
    # print(book_subquery)
    # stock = session.query(Stock).join(book_subquery, Stock.id ==


open_json()
session.close()
