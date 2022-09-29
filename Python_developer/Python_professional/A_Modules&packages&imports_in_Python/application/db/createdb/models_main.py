import sqlalchemy as sq
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()


class People(Base):
    __tablename__ = 'employees'

    id = sq.Column(sq.Integer, primary_key=True)
    first_name = sq.Column(sq.String(50), nullable=False)
    last_name = sq.Column(sq.String(50), nullable=False)

    def __str__(self):
        return f'(id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name})'


def create_db(cg):
    DATABASE_NAME = 'employees'
    DSN = f'postgresql://{cg.USER}:{cg.PASSWORD}@{cg.HOST}:{cg.PORT}/{DATABASE_NAME}'
    engine = sq.create_engine(DSN)
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return f'- db created'
