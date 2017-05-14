import datetime
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    DateTime,
    UnicodeText,
    desc,
)

from .meta import Base


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    body = Column(UnicodeText, default="", nullable=True)
    created = Column(DateTime, default=datetime.datetime.utcnow())
    edited = Column(DateTime, default=datetime.datetime.utcnow())

    @classmethod
    def all(cls, session):
        """Return all"""
        return session.query(cls).order_by(desc(cls.created)).all()

    @classmethod
    def by_id(cls, id, session):
        """Return entry by id number"""
        return session.query(cls).get(id)

