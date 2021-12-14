import marshmallow as ma

from marshmallow_enum import EnumField
from src.schemas.base import BaseModelSchema
from src.schemas.utilizations import UtilizationSchema
from src.models import ClaimLineItem


class ClaimLineItemSchema(BaseModelSchema):
    class Meta:
        strict = True
        ordered = True
        transient = True
        model = ClaimLineItem
        dump_only = ('id', 'claim_line_item_type', 'amount_claimed', 'quantity','decision','utilization')
        fields = dump_only

    decision = EnumField(ClaimLineItem.DecisionTypeEnum, by_value=True)
    claim_line_item_type = EnumField(ClaimLineItem.ClaimLineItemTypeEnum, by_value=True)
    utilization = ma.fields.Nested(UtilizationSchema, many=True)


class ClaimLineItemResponse(BaseModelSchema):
    strict = True
    ordered = True
    transient = True
    model = ClaimLineItem
    dump_only = ('id', 'claim_line_item_type')
    fields = dump_only

    id = ma.fields
    claim_line_item_type = EnumField(ClaimLineItem.ClaimLineItemTypeEnum, by_value=True)



