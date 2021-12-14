import uuid

from sqlalchemy import types
from sqlalchemy.dialects.mysql.base import MSBinary


class UUID(types.TypeDecorator):
    """UUID converter for Aurora database without native support for UUID types.

    This is a SQLAlchemy type converter that will allow for an easy conversion between binary and
    UUID values at the database interface.

    This function should be limited to the SQLAlchemy mixin definition. If looking to type hint,
    the standard uuid.UUID should be used.
    """
    impl = MSBinary

    def __init__(self, length=16):
        self.impl.length = 16
        types.TypeDecorator.__init__(self, length=self.impl.length)

    def process_bind_param(self, value, dialect=None):
        if value and isinstance(value, uuid.UUID):
            return value.bytes
        elif value and not isinstance(value, uuid.UUID):
            raise ValueError('value %s is not a valid uuid.UUID' % value)
        else:
            return None

    def process_result_value(self, value, dialect=None):
        if value:
            return uuid.UUID(bytes=value)
        else:
            return None

    def is_mutable(self):
        return False
