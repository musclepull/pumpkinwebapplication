import uuid

from sqlalchemy import Column

from ..fields import UUID


class UUIDidMixin(object):
    id = Column('id', UUID(), primary_key=True, default=uuid.uuid4)
