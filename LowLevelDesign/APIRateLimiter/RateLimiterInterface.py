import abc
from APIRateLimiter.Request import Request


class RateLimiterInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def grantAccess(self, request: Request):
        pass
