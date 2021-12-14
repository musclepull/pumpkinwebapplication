import arrow

from sqlalchemy import Column
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy_utils import ArrowType


class DateTimeMixin(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    created_at = Column(ArrowType, default=arrow.utcnow)
    updated_at = Column(ArrowType, onupdate=arrow.utcnow)
    deleted_at = Column(ArrowType)
