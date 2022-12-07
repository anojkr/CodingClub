
from KeyValueStore.models.Boolean import Boolean
from KeyValueStore.models.String import String
from KeyValueStore.models.Integer import Integer


class AttributeFactoryManager:

    @staticmethod
    def getValue(key, value):
        if isinstance(value, bool):
            return Boolean(key, value)
        elif isinstance(value, str):
            return String(key, value)
        elif isinstance(value, int):
            return Integer(key, value)
        else:
            raise Exception("InvalidTypeValue")
