from sqlalchemy import (Column, Integer)

from .base import Base
from .mixins import DateTimeMixin, UUIDidMixin


class Plan(Base, DateTimeMixin, UUIDidMixin):
    __tablename__ = 'plans'

    vaccines = Column(Integer, nullable=False)
    wellness_exam = Column(Integer, nullable=False)
    blood_test = Column(Integer, nullable=False)
