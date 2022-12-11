import threading

from APIRateLimiter.RateLimiter import RateLimiter
from Request import Request

def apiLimiterDriver():
    rateLimiter = RateLimiter(1, 1)
    res = []
    request = Request("172.0.0.1", "mac-os-1").setTime()
    for i in range(5):
        # r = threading.Thread(target=rateLimiter.isRequestAllowed, args=[request])
        # r.start()
        response = rateLimiter.grantAccess(request)
        print(response)
    #     res.append(r)
    #     print(r)
    # e = [r.join() for _ in res]
    # print(e)


if __name__ == "__main__":
    apiLimiterDriver()