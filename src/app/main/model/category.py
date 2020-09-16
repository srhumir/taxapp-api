from .. import db
from sqlalchemy import BigInteger, Column, DateTime,ForeignKey, Text, text
from sqlalchemy.orm import relationship
from .relations import HIBERNATE_SEQUENCE
Base = db.Model
metadata = Base.metadata


class Category(Base):
    __tablename__ = 'category'

    id = Column(BigInteger, primary_key=True,
                server_default=HIBERNATE_SEQUENCE.next_value())
    version = Column(BigInteger, nullable=False, server_default=text("0"))
    lastmodified = Column(DateTime(True), nullable=False,
                          server_default=text("statement_timestamp()"))
    created = Column(DateTime(True), nullable=False,
                     server_default=text("statement_timestamp()"))
    categorytype = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    customerid = Column(ForeignKey('customer.id'), nullable=False)

    customer = relationship('Customer')
