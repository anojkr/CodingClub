
from KeyValueStore.models.Boolean import Boolean
from KeyValueStore.models.String import String
from KeyValueStore.models.Integer import Integer


class AttributeFactoryManager:

    @staticmethod
    def getValue(value):
        if isinstance(value, bool):
            return Boolean(value)
        elif isinstance(value, str):
            return String(value)
        elif isinstance(value, int):
            return Integer(value)
        else:
            raise Exception("InvalidTypeValue")