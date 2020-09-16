from .. import db
from sqlalchemy import BigInteger,Column, DateTime, ForeignKey, LargeBinary, Text, text
from sqlalchemy.orm import relationship
from .relations import HIBERNATE_SEQUENCE

Base = db.Model
metadata = Base.metadata


class File(Base):
    __tablename__ = 'file'

    id = Column(BigInteger, primary_key=True,
                server_default=HIBERNATE_SEQUENCE.next_value())
    version = Column(BigInteger, nullable=False, server_default=text("0"))
    lastmodified = Column(DateTime(True), nullable=False,
                          server_default=text("statement_timestamp()"))
    created = Column(DateTime(True), nullable=False, server_default=text("statement_timestamp()"))
    customerid = Column(ForeignKey('customer.id'), nullable=False)
    businessid = Column(ForeignKey('business.id'))
    filetype = Column(Text, nullable=False)
    content = Column(LargeBinary, nullable=False)
    filename = Column(Text, nullable=False)
    description = Column(Text)

    busines = relationship('Busines')
    customer = relationship('Customer')
