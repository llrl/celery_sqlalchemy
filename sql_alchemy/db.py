from sqlalchemy import create_engine
from sqlalchemy import (MetaData, String, Integer, CHAR, Column, Table, ForeignKey)

engine = create_engine('sqlite:///database.db', echo=True)

metadata = MetaData()

files = Table('files', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String)
              )


def connection():
    global engine
    return engine.connect()


def migrate():
    global metadata
    global engine
    metadata.create_all(engine)
