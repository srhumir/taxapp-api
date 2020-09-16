from .. import db
from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, Text, text
from sqlalchemy.orm import relationship
from .category import Category
from .consultant import Consultant
from .customer import Customer
from .relations import HIBERNATE_SEQUENCE

Base = db.Model
metadata = Base.metadata
print('business')


class Busines(Base):
    __tablename__ = 'business'

    id = Column(BigInteger, primary_key=True,
                server_default=HIBERNATE_SEQUENCE.next_value())
    version = Column(BigInteger, nullable=False, server_default=text("0"))
    lastmodified = Column(DateTime(True), nullable=False,
                          server_default=text("statement_timestamp()"))
    created = Column(DateTime(True), nullable=False, server_default=text("statement_timestamp()"))
    customerid = Column(ForeignKey('customer.id'), nullable=False)
    consultantid = Column(ForeignKey('consultant.id'))
    name = Column(Text, nullable=False)
    email = Column(Text, nullable=True)
    phone = Column(Text, nullable=True)
    web = Column(Text, nullable=True)
    active = Column(Boolean, nullable=False, server_default=text("true"))
    type = Column(Text, nullable=False)
    categoryid = Column(ForeignKey('category.id'))
    peridicalsend = Column(Boolean, server_default=text("false"))
    peridicaldate = Column(DateTime)

    category = relationship(Category)
    consultant = relationship(Consultant)
    customer = relationship(Customer)


class BusinesHistory(Base):
    __tablename__ = 'business_history'

    id = Column(BigInteger, primary_key=True, autoincrement=False)
    version = Column(BigInteger, primary_key=True, autoincrement=False)
    lastmodified = Column(DateTime(True), nullable=False,
                          server_default=text("statement_timestamp()"))
    created = Column(DateTime(True), nullable=False, server_default=text("statement_timestamp()"))
    customerid = Column(ForeignKey('customer.id'), nullable=False)
    consultantid = Column(ForeignKey('consultant.id'))
    name = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    phone = Column(Text, nullable=True)
    web = Column(Text, nullable=False)
    active = Column(Boolean, nullable=False, server_default=text("true"))
    type = Column(Text, nullable=False)
    categoryid = Column(ForeignKey('category.id'))
    peridicalsend = Column(Boolean, server_default=text("false"))
    peridicaldate = Column(DateTime)

    category = relationship(Category)
    consultant = relationship(Consultant)
    customer = relationship(Customer)
