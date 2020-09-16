from .. import db
from sqlalchemy import BigInteger, Boolean, Column, DateTime, Float, ForeignKey, \
    LargeBinary, Text, text
from sqlalchemy.orm import relationship
from .relations import HIBERNATE_SEQUENCE

Base = db.Model
metadata = Base.metadata


class Invoice(Base):
    __tablename__ = 'invoice'

    id = Column(BigInteger, primary_key=True,
                server_default=HIBERNATE_SEQUENCE.next_value())
    version = Column(BigInteger, nullable=False, server_default=text("0"))
    lastmodified = Column(DateTime(True), nullable=False,
                          server_default=text("statement_timestamp()"))
    created = Column(DateTime(True), nullable=False, server_default=text("statement_timestamp()"))
    customerid = Column(ForeignKey('customer.id'), nullable=False)
    businessid = Column(ForeignKey('business.id'))
    categoryid = Column(ForeignKey('category.id'))
    uniquecode = Column(Text, nullable=False)
    amount = Column(Float(53), nullable=False)
    amountexvat = Column(Float(53), nullable=False)
    merchantname = Column(Text, nullable=False)
    tags = Column(Text, nullable=False)
    image = Column(LargeBinary)
    issuedate = Column(DateTime)
    sent = Column(Boolean, server_default=text("false"))
    fulljson = Column(Text, nullable=False, server_default=text("''::text"))

    busines = relationship('Busines')
    category = relationship('Category')
    customer = relationship('Customer')
