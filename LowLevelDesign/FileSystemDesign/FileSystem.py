from abc import ABCMeta, abstractmethod


class FileSystem(metaclass=ABCMeta):

    @abstractmethod
    def ls(self):
        pass
