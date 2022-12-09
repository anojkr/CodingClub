from KeyValueStore.models.AttributeValueInterface import AttributeValueInterface


class Boolean(AttributeValueInterface):

    def __init__(self):
        self.value: bool = None

    def setValue(self, value: bool):
        self.value = value
        return self

    def getValue(self):
        return self.value
