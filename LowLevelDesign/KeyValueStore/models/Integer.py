from KeyValueStore.models.AttributeValueInterface import AttributeValueInterface


class Integer(AttributeValueInterface):

    def __init__(self):
        self.key: str = None
        self.value: int = None

    def setKey(self, key: str):
        self.key = key

    def setValue(self, value: int):
        self.value = value

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value
