from KeyValueStore.models.AttributeValueInterface import AttributeValueInterface


class Boolean(AttributeValueInterface):

    def __init__(self, value):
        self.value: bool = value

    def setValue(self, value: bool):
        self.value = value

    def getValue(self):
        return self.value
