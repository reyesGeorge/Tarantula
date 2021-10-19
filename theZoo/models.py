from typing import Text
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import  String, TEXT


from theZoo import settings

DeclarativeBase = declarative_base()



def db_connect() -> Engine:
    
    """
    Creates database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """    

    return create_engine(URL(**settings.DATABASE))


def create_items_table(engine: Engine):
    """
    Create the Items table
    """
    DeclarativeBase.metadata.create_all(engine)


class Items(DeclarativeBase):
    """
    Defines the items model
    """

    __tablename__ = "items"

    # TABLE COLUMNS
    id = Column("id", Integer, primary_key=True)
    text = Column("text", TEXT)
    author = Column("author", String)
    tags = Column("tags", TEXT)
    spider = Column("spider", String)
