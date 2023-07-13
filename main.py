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


def searching():
    data = input('Input publisher name ')
    for el in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)\
            .join(Publisher)\
            .join(Stock)\
            .join(Shop)\
            .join(Sale)\
            .filter(Publisher.name == data).all():
        name_book, name_shop, price, date_sale = el
        print(f'{name_book} | {name_shop} | {price} | {date_sale}')


open_json()
searching()
session.close()
