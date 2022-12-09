from KeyValueStore.models.Boolean import Boolean
from KeyValueStore.models.String import String
from KeyValueStore.models.Integer import Integer


class AttributeFactoryManager(object):
    attributeMap = {}

    def __init__(self):
        self.__class__.attributeMap = {
            bool: Boolean(),
            str: String(),
            int: Integer()
        }

    def getAttributeProvider(self, type):
        return self.__class__.attributeMap.get(type)
