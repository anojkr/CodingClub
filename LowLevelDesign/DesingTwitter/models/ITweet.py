import abc

class ITweet(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getTweetId(self):
        pass

    @abc.abstractmethod
    def getUserId(self):
        pass

    @abc.abstractmethod
    def getComments(self):
        pass