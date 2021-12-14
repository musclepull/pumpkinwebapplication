from marshmallow import post_dump
from marshmallow_sqlalchemy import ModelSchema, ModelSchemaOpts


class BaseModelSchemaOpts(ModelSchemaOpts):

    def __init__(self, meta):
        super().__init__(meta)


class BaseModelSchema(ModelSchema):
    OPTIONS_CLASS = BaseModelSchemaOpts

    def on_bind_field(self, field_name, field_obj):
        super().on_bind_field(field_name, field_obj)


class BaseResponseSchema:
    @post_dump(pass_many=True)
    def add_envelope(self, data, many):
        return {
            "error": False,
            "body": {
                "data": data
            }
        }
