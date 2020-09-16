from .. import db
from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, Text, text
from sqlalchemy.orm import relationship
from .relations import HIBERNATE_SEQUENCE

Base = db.Model
metadata = Base.metadata
print('consultant')


class Consultant(Base):
    __tablename__ = 'consultant'

    id = Column(BigInteger, primary_key=True,
                server_default=HIBERNATE_SEQUENCE.next_value())
    version = Column(BigInteger, nullable=False, server_default=text("0"))
    lastmodified = Column(DateTime(True), nullable=False,
                          server_default=text("statement_timestamp()"))
    created = Column(DateTime(True), nullable=False,
                     server_default=text("statement_timestamp()"))
    name = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    web = Column(Text, nullable=False)
    address = Column(Text, nullable=False)
    active = Column(Boolean, nullable=False, server_default=text("true"))
    customerid = Column(ForeignKey('customer.id'), nullable=False)

    customer = relationship('Customer')
