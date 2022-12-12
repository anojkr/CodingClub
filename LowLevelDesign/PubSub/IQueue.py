import abc

class IQueue(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getTopicById(self, topicId=None):
        pass