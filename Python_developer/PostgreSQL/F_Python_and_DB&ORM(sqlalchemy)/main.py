import sqlalchemy as sq
import config as cg
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale
from sqlalchemy_utils import database_exists, create_database
import json


DATABASE_NAME = 'book_store'
DSN = f'postgresql://{cg.USER}:{cg.PASSWORD}@{cg.HOST}:{cg.PORT}/{DATABASE_NAME}'
engine = sq.create_engine(DSN)
if not database_exists(engine.url):
    create_database(engine.url)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

publisher = input(f'Enter id or publisher name: ')

with open('tests_data.json', 'r') as f:
    DATA = json.load(f)


def load_data(data):
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


load_data(DATA)


def publisher_request(input_p):
    if input_p.isdigit():
        query = session.query(Publisher).filter(Publisher.id == input_p).all()
    else:
        query = session.query(Publisher).filter(Publisher.name == input_p).all()
    if query:
        for output in query:
            return output
    return 'Publisher not found'


def shop_request(input_p):
    query = session.query(Shop)
    query = query.join(Stock)
    query = query.join(Book)
    query = query.join(Publisher)
    if input_p.isdigit():
        query = query.filter(Publisher.id == input_p).all()
    else:
        query = query.filter(Publisher.name == input_p).all()
    if query:
        for output in query:
            return output
    return 'Publisher not found'


print(publisher_request(publisher))
print(shop_request(publisher))

session.close()
