import marshmallow as ma

from marshmallow_enum import EnumField
from src.schemas.base import BaseModelSchema
from src.models import Utilization

class UtilizationSchema(BaseModelSchema):
    class Meta:
        strict = True
        ordered = True
        transient = True
        model = Utilization
        dump_only = ('id', 'utilized', 'total')
        fields = dump_only

        utilized = ma.fields
        total = ma.fields


