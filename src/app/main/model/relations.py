from main import db
from sqlalchemy import Column, Text, Sequence

Base = db.Model
metadata = Base.metadata

HIBERNATE_SEQUENCE = Sequence('hibernate_sequence', start=1, increment=1, cache=1)

t_version = db.Table(
    'version', metadata,
    Column('version', Text, nullable=False),
    extend_existing=True
)
