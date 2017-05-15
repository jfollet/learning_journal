from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
)

from .meta import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(255), nullable=False, unique=True, index=True)
    password = Column(UnicodeText, nullable=False)

    @classmethod
    def user(cls, username, session):
        return session.query(cls).filter(cls.username == username)
