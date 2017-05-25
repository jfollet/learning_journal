from passlib.context import CryptContext
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
)

password_context = CryptContext(['pbkdf2_sha512'])

from .meta import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(255), nullable=False, unique=True, index=True)
    password = Column(UnicodeText, nullable=False)

    @classmethod
    def by_name(cls, username, session):
        return session.query(cls).filter(cls.username == username).first()

    def verify_password(self, password):
        return password_context.verify(password, self.password)
