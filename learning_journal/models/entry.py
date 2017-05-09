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


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    body = Column(UnicodeText, nullable=True)
    created = Column(DateTime, default=datetime.datetime.utcnow())
    edited = Column(DateTime,  default=datetime.datetime.utcnow())

    @classmethod
    def all(cls, session):
        """Return all"""
        return session.query(Entry).order_by(desc(Entry.created))

    @classmethod
    def by_id(cls, session, id):
        """Return entry by id number"""
        return session.query(Entry).get(id)


# Index('my_index', Entry.title, unique=True, mysql_length=255)
