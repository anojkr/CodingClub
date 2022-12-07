from KeyValueStore.models.AttributeValueInterface import AttributeValueInterface


class String(AttributeValueInterface):

    def __init__(self, value):
        self.value: str = value

    def setValue(self, value: str):
        self.value = value

    def getValue(self):
        return self.value
