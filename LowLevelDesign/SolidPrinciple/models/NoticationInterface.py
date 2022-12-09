import abc


class NotificationInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def sendNotification(self):
        pass
