from sqlalchemy import (
    Column,
    Index,
    Integer,
    UnicodeText,
    DateTime
)

from .meta import Base


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(UnicodeText)
    body = Column(Integer)
    created = Column(DateTime)
    edited = Column(DateTime)

    def all(self):
        """Return all entries in database"""
        pass

    def by_id(self, id):
        """Return entry by id number"""
        pass
    

Index('my_index', Entry.name, unique=True, mysql_length=255)
