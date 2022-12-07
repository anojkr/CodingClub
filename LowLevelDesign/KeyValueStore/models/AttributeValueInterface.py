import abc


class AttributeValueInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def setValue(self, value):
        pass

    @abc.abstractmethod
    def getValue(self):
        pass
