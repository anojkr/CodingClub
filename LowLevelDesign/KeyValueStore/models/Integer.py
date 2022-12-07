from KeyValueStore.models.AttributeValueInterface import AttributeValueInterface


class Integer(AttributeValueInterface):

    def __init__(self, value):
        self.value: int = value

    def setValue(self, value: int):
        self.value = value

    def getValue(self):
        return self.value
