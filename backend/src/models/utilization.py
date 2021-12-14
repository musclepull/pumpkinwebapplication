import enum

from sqlalchemy import (Column, Enum, ForeignKey, Integer)
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean

from .base import Base
from .fields import UUID
from .mixins import DateTimeMixin, UUIDidMixin


class Utilization(Base, DateTimeMixin, UUIDidMixin):
    __tablename__ = 'utilization'

    utilized = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)

    claim_line_item = relationship("ClaimLineItem", back_populates='line_items')
    claim_line_items_id = Column(UUID(), ForeignKey('claim_line_items.id'), nullable=False)
