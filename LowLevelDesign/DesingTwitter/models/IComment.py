import abc

class IComment(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getCommentId(self):
        pass

    @abc.abstractmethod
    def getUserId(self):
        pass

    @abc.abstractmethod
    def getTweetId(self):
        pass