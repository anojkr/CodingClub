import abc

class MeetingRoom(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getId(self):
        pass

    @abc.abstractmethod
    def getCapacity(self):
        pass

    @abc.abstractmethod
    def setCapacity(self):
        pass

    @abc.abstractmethod
    def getRoomType(self):
        pass
