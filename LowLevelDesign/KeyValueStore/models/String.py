from KeyValueStore.models.AttributeValueInterface import AttributeValueInterface


class String(AttributeValueInterface):

    def __init__(self):
        self.key: str = None
        self.value: str = None

    def setKey(self, key: str):
        self.key = key

    def setValue(self, value: str):
        self.value = value

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value
