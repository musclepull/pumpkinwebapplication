import enum
from typing import List

from sqlalchemy import (Column, Enum, ForeignKey, Integer)
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean
from .utilization import Utilization

from .base import Base
from .fields import UUID
from .mixins import DateTimeMixin, UUIDidMixin


class ClaimLineItem(Base, DateTimeMixin, UUIDidMixin):
    __tablename__ = 'claim_line_items'

    class ClaimLineItemTypeEnum(enum.Enum):
        vaccine = 'Vaccine'
        wellness_exam = 'Wellness Exam'
        blood_test = 'Blood Test'

    class DecisionTypeEnum(enum.Enum):
        approved = 'Approved'
        denied = 'Denied'

    amount_claimed = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    decision = Column(Enum(DecisionTypeEnum), nullable=False)
    claim_line_item_type = Column(Enum(ClaimLineItemTypeEnum), nullable=True)

    line_items: List[Utilization] = relationship(
    "Utilization",
    order_by='ClaimLineItem.created_at',
    cascade="save-update, merge, delete")

    claim = relationship("Claim", back_populates='line_items')
    claim_id = Column(UUID(), ForeignKey('claims.id'), nullable=False)
