from abc import ABCMeta, abstractmethod


class RateLimiter(metaclass=ABCMeta):

    @abstractmethod
    def grantAccess(self):
        pass
