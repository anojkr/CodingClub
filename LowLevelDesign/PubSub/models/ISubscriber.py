import abc

class ISubscriber(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getSubscriberId(self):
        pass
