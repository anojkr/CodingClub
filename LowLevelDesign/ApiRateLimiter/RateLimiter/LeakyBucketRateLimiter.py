from RateLimiter.RateLimiter import RateLimiter
import threading
import collections


class LeakyBucketRateLimiter(RateLimiter):

    def __init__(self, bucketSize):
        self.queue = collections.deque()
        self.bucketSize = bucketSize
        self._lock = threading.Lock()

    def grantAccess(self, request):
        with self._lock:
            if len(self.queue) < self.bucketSize:
                self.queue.append(request)
                return True
            else:
                return False
