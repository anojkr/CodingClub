from collections import defaultdict, deque
from Request import Request
import time
import threading
from APIRateLimiter.RateLimiterInterface import RateLimiterInterface

class SlidingWindowRateLimiter(RateLimiterInterface):

    SlidingWindowMap = None

    def __init__(self, capacity, timeLimit):
        self.__class__.SlidingWindowMap = defaultdict(deque)
        self.capacity = capacity
        self.timeInSec = timeLimit
        self._lock = threading.Lock()

    def grantAccess(self, request: Request):
        with self._lock:
            return self.isRequestAllowed(request)

    def isRequestAllowed(self, req: Request):
        slidingWindowMap = self.__class__.SlidingWindowMap
        uniqueId = (req.deviceId, req.ip)
        if uniqueId not in slidingWindowMap:
            slidingWindowMap[uniqueId].append(req)
            return True
        else:
            requests = slidingWindowMap[uniqueId]
            timeLimit = self.getTimeLimitEpocMilli()
            while len(requests) > 0 and requests[0].time < timeLimit:
                if requests[0].time < timeLimit:
                    requests.popleft()
            if len(requests) < self.capacity:
                requests.append(req)
                return True
            else:
                return False

    def getTimeLimitEpocMilli(self):
        return int(time.time()) * 1000 - self.timeInSec


