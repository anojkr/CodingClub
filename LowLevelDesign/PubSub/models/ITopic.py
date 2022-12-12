import abc

class ITopic(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getTopicId(self):
        pass

    @abc.abstractmethod
    def getTopicSubscribers(self):
        pass

    @abc.abstractmethod
    def getAllMessages(self):
        pass