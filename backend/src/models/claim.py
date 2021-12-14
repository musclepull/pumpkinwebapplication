import enum
from typing import List

from sqlalchemy import Column, Enum, ForeignKey,Integer
from sqlalchemy.orm import relationship

from .base import Base
from .claim_line_item import ClaimLineItem
from .fields import UUID
from .mixins import DateTimeMixin, UUIDidMixin


class Claim(Base, DateTimeMixin, UUIDidMixin):
    __tablename__ = 'claims'

    class ClaimTypeEnum(enum.Enum):
        prevent = 'Prevent'
        protect = 'Protect'

    claim_type = Column(Enum(ClaimTypeEnum), nullable=False)

    plan = relationship("Plan")
    plan_id = Column(UUID(), ForeignKey('plans.id'), nullable=False)

    line_items: List[ClaimLineItem] = relationship(
        "ClaimLineItem",
        order_by='ClaimLineItem.created_at',
        cascade="save-update, merge, delete")

    @property
    def amount_claimed(self):
        return sum([line_item.amount_claimed for line_item in self.line_items])
