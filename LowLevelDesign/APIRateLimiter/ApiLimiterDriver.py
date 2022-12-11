import threading
import time

from APIRateLimiter.SlidingWindowRateLimiter import SlidingWindowRateLimiter
from Request import Request

def apiLimiterDriver():
    rateLimiter = SlidingWindowRateLimiter(1, 1)
    request = Request("172.0.0.1", "mac-os-1").setTime()
    """
        result = []
        thread = []
        for i in range(10):
            thread.append(threading.Thread(target=rateLimiter.grantAccess, args=[request]))
        [_.start() for _ in thread]
        e = [_.join() for _ in thread]
        print(e)
    """
    for i in range(10):
        r = rateLimiter.grantAccess(request)
        print(r)

if __name__ == "__main__":
    apiLimiterDriver()