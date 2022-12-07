from KeyValueStore.models.AttributeValueInterface import AttributeValueInterface


class Boolean(AttributeValueInterface):

    def __init__(self):
        self.key: str = None
        self.value: bool = None

    def setKey(self, key: str):
        self.key = key

    def setValue(self, value: bool):
        self.value = value

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value
