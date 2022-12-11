from collections import defaultdict, deque
from Request import Request
import time
import threading

class RateLimiter(object):

    RateLimit = None

    def __init__(self, capacity, timeLimit):
        self.__class__.RateLimit = defaultdict(deque)
        self.capacity = capacity
        self.timeInSec = timeLimit
        self._lock = threading.Lock()

    def grantAccess(self, request: Request):
        with self._lock:
            return self.isRequestAllowed(request)

    def isRequestAllowed(self, newRequest: Request):
        rateLimiter = self.__class__.RateLimit
        uniqueId = (newRequest.deviceId, newRequest.ip)
        if uniqueId not in rateLimiter:
            rateLimiter[uniqueId].append(newRequest)
            return True
        else:
            requests = rateLimiter[uniqueId]
            timeLimit = self.getTimeLimitEpocMilli()
            while len(requests) > 0 and requests[0].time < timeLimit:
                if requests[0].time < timeLimit:
                    requests.popleft()
            if len(requests) < self.capacity:
                requests.append(newRequest)
                return True
            else:
                return False

    def getTimeLimitEpocMilli(self):
        return int(time.time()) * 1000 - self.timeInSec


