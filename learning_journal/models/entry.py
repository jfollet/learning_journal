from sqlalchemy import (
    Column,
    Index,
    Integer,
    Unicode,
    DateTime,
    UnicodeText,
    desc,
)
import datetime

from .meta import Base

import sqlalchemy as sa

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    body = Column(UnicodeText, default="", nullable=True)
    created = Column(DateTime, default=datetime.datetime.utcnow())
    edited = Column(DateTime,  default=datetime.datetime.utcnow())

    @classmethod
    def all(cls, session):
        """Return all"""
        return session.query(cls).order_by(desc(cls.created))

    @classmethod
    def by_id(cls, session, id):
        """Return entry by id number"""
        return session.query(cls).get(id)


# Index('my_index', Entry.title, unique=True, mysql_length=255)
