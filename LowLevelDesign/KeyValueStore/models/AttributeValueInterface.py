import abc


class AttributeValueInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def setKey(self, key):
        pass

    @abc.abstractmethod
    def setValue(self, value):
        pass

    @abc.abstractmethod
    def getKey(self):
        pass

    @abc.abstractmethod
    def getValue(self):
        pass

