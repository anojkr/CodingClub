
"""
    Reference :
        1. https://blog.tryexponent.com/rate-limiter-system-design/
        2. https://konghq.com/blog/how-to-design-a-scalable-rate-limiting-algorithm
        3. https://www.enjoyalgorithms.com/blog/design-api-rate-limiter
        4. https://leetcode.com/discuss/interview-question/system-design/1616482/System-Design%3A-Rate-Limiter
        5. https://youtu.be/mhUQe4BKZX
"""

from RateLimiter.LeakyBucketRateLimiter import LeakyBucketRateLimiter
def main():
    s = LeakyBucketRateLimiter(1)
    s.grantAccess(request="1")
    s.grantAccess(request="1")

if __name__ == "__main__":
    main()
