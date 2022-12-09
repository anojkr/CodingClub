from KeyValueStore.models.AttributeValueInterface import AttributeValueInterface


class String(AttributeValueInterface):

    def __init__(self):
        self.value: str = None

    def setValue(self, value: str):
        self.value = value
        return self

    def getValue(self):
        return self.value
