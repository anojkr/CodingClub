from abc import ABCMeta, abstractmethod


class RateLimiterDAO(metaclass=ABCMeta):

    @abstractmethod
    def grantAccess(self):
        pass









