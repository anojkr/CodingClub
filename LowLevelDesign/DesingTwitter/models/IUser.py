
import abc

class IUser(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getUserId(self):
        pass

    @abc.abstractmethod
    def getFollowers(self):
        pass

    @abc.abstractmethod
    def getFollowees(self):
        pass

    @abc.abstractmethod
    def addFollowee(self, user):
        pass

    @abc.abstractmethod
    def addFollower(self, user):
        pass