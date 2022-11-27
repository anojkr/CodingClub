Design: https://drive.google.com/file/d/1j54pl2YF10YVME-O1riRw1LQtdCOQitM/view?usp=sharing
```
Rate Limiting is a process that is used to define the rate and speed at which consumers can access 
APIs. Throttling is the process of controlling the usage of the APIs by customers during a given 
period. When a throttle limit is crossed, the server returns HTTP status “429 - Too many requests"

Advantages
    - Prevent DDOS attack
    - Prevent unnecessary resource utilisation
    - Eliminate peak traffic

1. Functional Requirement
    - Client Side or server side rate limitting?
    - Limit the number of requests an entity can send to an API within a time window
    - The user should get an error message whenever the defined threshold is crossed
    
2. Non-Functional Requirement
    - Highly Available
    - Should not effect user experiance with latency
    
3. Capacity Estimation
    Assumntion, we rate limit 500 request per/hour
    Sliding Window
        8 byte(userId) + (4 byte(epocTime) + 20 byte(sortedSet))*500 + 20 byte(HashTable) => 12 KB
        If we track 1 million user at any given time
            12 KB * 10^6 => 12 GB
        
4. Architecture deep-dive

    API:
        requestAllowed(userId, ipAddress)
        
    Rate Limiting by IPAddress or User
        - IPAddress: Issue when mutiple users using same IP. Eg. University, CyberCafe
        - User: User authentication needed, but we have to rate-limit on login atttempt itself
        - Hybri: IP+User -> Combining both will solve the problem
    
    Database Sharding
        - userId     
    
          
    Fixed window algorithm:
    
        {
           "userId":{
              "startime":"epocTimeStamp",
              "count":"5
                    limit":10
           }
        }
    
        1. If userId not in HashTble, insert new record with key=userId and startTime=currentEpocTime, count=1
        2. Otherwise, find userId and if currTime-startTime >= 1 minute, set startTime= currentTime and count=1
        3  If currentTime - startTime <= 1 minute:
            - If count < limit, increment counter and allow request
            - elseIF count >= limitreject request
        Cons:
            - Race condition issue in distributed system(Two server read at same time)
            - Locks can be used to solve issue, but it will take preformance hit   
            - Cluster of request around boundary
            
    Sliding window alogirthm:
        We can maintain a sliding window if we can keep track of each request per user. We can store the 
        timestamp of each request in a Redis Sorted Set in our ‘value’ field of hash-table.

            {
               "userA": SortedLinkList[
                  {
                     "requestId":"1",
                     "timeStamp":"epocTime"
                  }
               ],
               
               "userB": SortedLinkList[
                  {
                     "requestId":"1",
                     "timeStamp":"epocTime"
                  }
               ],
            }
        
        Let’s assume our rate limiter is allowing three requests per minute per user, so, whenever a new request
        comes in, the Rate Limiter will perform following steps:
        
            1. Remove all the timestamps from the Sorted Set that are older than “CurrentTime - 1 minute”.
            2. Count the total number of elements in the sorted set. Reject the request if this count is greater 
            than our throttling limit of “3”.
            3. Insert the current time in the sorted set and accept the request
            
        Component Design
            - RateLimiter Service
            - Redis Cache(Store HashMap of user-request)
            - Database(Rate-limiting rule)
            - Service server(reservation, userprofile, cab-booking etc.)
        
            Steps
            • Rate limiting rules are stored on the disk. Workers frequently pull rules from the disk and store them in the cache.
            • When a client sends a request to the server, the request is sent to the rate limiter middleware first.
            • Rate limiter middleware loads rules from the cache. It fetches counters and last request timestamp from Redis cache. Based on the response, the rate limiter decides
            • if the request is not rate limited, it is forwarded to API servers. 
            • if the request is rate limited, the rate limiter returns 429 too many requests error to the client. In the meantime, the request is either dropped or forwarded to the queue
            
            Rate limiter in a distributed environment
                Building a rate limiter that works in a single server environment is not difficult. However,
                scaling the system to support multiple servers and concurrent threads is a different story.
                There are two challenges:
                • Race condition
                • Synchronization issue
            
            Solution:
                - Sticky session: 
                    When you introduce a sticky session in your load balancers, each consumer gets sent to exactly one node. 
                    The downside to this strategy includes a lack of fault tolerance and scaling problems when nodes get overloaded.
                - Centralized data store: 
                    You can use a centralized data store like Redis or Cassandra to handle counts for each window and consumer. 
                    While this adds latency, the flexibility it provides makes it an elegant solution.
```