from KeyValueStore.models.AttributeValueInterface import AttributeValueInterface


class Integer(AttributeValueInterface):

    def __init__(self):
        self.value: int = None

    def setValue(self, value: int):
        self.value = value
        return self

    def getValue(self):
        return self.value
