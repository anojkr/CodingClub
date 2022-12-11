import abc

class BookEvent(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def bookEvent(self):
        pass