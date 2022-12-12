import abc

class IMessage(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getMessageId(self):
        pass

    @abc.abstractmethod
    def setMessageStatus(self):
        pass

    @abc.abstractmethod
    def getMessageStatus(self):
        pass