from main import db
from sqlalchemy import BigInteger, Boolean, Column, DateTime, LargeBinary, Text, text
from .relations import HIBERNATE_SEQUENCE

Base = db.Model
metadata = Base.metadata
print('customer')


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(BigInteger, primary_key=True,
                server_default=HIBERNATE_SEQUENCE.next_value())
    version = Column(BigInteger, nullable=False,
                     server_default=text("0"))
    lastmodified = Column(DateTime(True), nullable=False,
                          server_default=text("statement_timestamp()"))
    created = Column(DateTime(True), nullable=False, server_default=text("statement_timestamp()"))
    title = Column(Text, nullable=False)
    salutation = Column(Text, nullable=False)
    firstname = Column(Text, nullable=False)
    lastname = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    mobile = Column(Text, nullable=False)
    active = Column(Boolean, nullable=False, server_default=text("true"))
    username = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    avatar = Column(LargeBinary)


class CustomerHistory(Base):
    __tablename__ = 'customer_history'

    id = Column(BigInteger, primary_key=True, autoincrement=False)
    version = Column(BigInteger, nullable=False, primary_key=True, autoincrement=False)
    lastmodified = Column(DateTime(True), nullable=False,
                          server_default=text("statement_timestamp()"))
    created = Column(DateTime(True), nullable=False,
                     server_default=text("statement_timestamp()"))
    title = Column(Text, nullable=False)
    salutation = Column(Text, nullable=False)
    firstname = Column(Text, nullable=False)
    lastname = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    mobile = Column(Text, nullable=False)
    active = Column(Boolean, nullable=False, server_default=text("true"))
    username = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    avatar = Column(LargeBinary)

