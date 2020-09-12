from main import db, flask_bcrypt
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
    password_hash = Column(Text, nullable=True)
    avatar = Column(LargeBinary)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)


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
    password_hash = Column(Text, nullable=False)
    avatar = Column(LargeBinary)

