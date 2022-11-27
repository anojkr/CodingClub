
Clarifying Questions?
Given a problem, Please gather requirement
```
1. Functional  Requirement
   - Given URL, generate unique tiny-url for each request
   - When tiny-url hit, redirect to original-url
   - Option to generate custom-url
   - Option to select custom expiry of short-url
   - Analytics(number of times url-hits, capture regions)

2. Non-Functional Requirement
   - Read latency should be very low
   - Short-url should not be easly predictable

3. Estimation of Scale
   Input
      -> 500 Million new url shorting request per month
      -> 100: 1 = read:write

   WriteQps => 500 x 10^6 / 26 x 10^5 => 200 request/sec
   ReadQps  => 20000 request/sec

   Storage Estimation
        (500 x 10^6) x  12 Months x 5 year => 30 x 10^9 => 30 billion url will  generate in 5 year
        Assuming size of each url -> 500 bytes
        30 billion x 500 bytes => 15 x 10^9 =  15 TB Storage required

   Bandwidth Estimation
        Incoming request -> (200 url/sec) x 500 bytes => 100 x 10^3 => 100 kbps bandwidth required
        Outgoing request -> (20 x 10^3 url/sec) x 500 bytes => 10 x 10^6 => 10 mbps bandwidth required

   CacheMemory Estimation -> 20 x 10^6 request/sec
        No of request in a day -> 20 x 10^6 x 24 x 3600 => 1.7 x 10^9 request/day
        Using 80-20 principle -> 20% of request are frequently used
            => 0.2 x 1.7 x 10^9 x 500 byte => 170 GB

3. Architecture deep-dive
    3 Tier-Architecture
        - Presentation Layer (UI)
        - Application Layer  (BackendAPI/Services) [Shortening-service, Redirection-service]
        - Data Storage Layer (Database Storage) [MySql]

    API :  generateShortUrl/{originalUrl}
           getOriginalUrl/{shortUrl}

    DatabaseSchema:
        URL(short_url, original_url, creation_date, userId, status)
        User(name, email, creationDate, lastLogin)

    How to handle Bottleneck
        - Size of database become large, contains billions of row. Query will become expensive. Solution [Database Sharding with Consistent Hashing]
        - Database corruption or failed node. Solution: [Master-Slave method]

    Database Sharding:
        Possible sharding-key
        - urlStart letter [A-Z]  -> Hot box issue (If one box get more data then others)
        - mod Hashing -> Cascading failure in  case of  any one instance down
        - Consistent Hashing -> works fine

    Master-Slave with Two Replica
    Master will handle write and replica for read

    Caching: Store hot short-url in redis-cache

    ShorteningService Logic:
        SecondInDay = 24*3600
        SecondInMonth = 30*24*3600
        First Approach :
            base64Encoding(md5Hash(originalUrl)) -> selecting first 6 char for short-url
            If two user try to get shortUrl for same-original-url, both will get same short-url
                - Custom expiry is not possible
                - Cannot record hits and measure analytics for user generated  short-url
                Ajay -> base64Encoding(md5Hash(www.facebook.com))  -> az43op  -> setExpiry(24*3600)
                Vijay -> base64Encoding(md5Hash(www.facebook.com)) -> az43op  -> setExpiry(SecondInMonth)

        Second Approach ->  Solution for above problem, add some unique key with original url
                Ajay -> base64Encoding(md5Hash(www.facebook.com + uniqueKey))  -> rctu90  -> setExpiry(24*3600)
                Vijay -> base64Encoding(md5Hash(www.facebook.com + uniqueKey)) -> az43op  -> setExpiry(SecondInMonth)
                Possible unique key:
                    - userId => Cannot work, As it failed for anonymous/non-login user
                    - Random-String -> Might work

    Offline Key Generation Service:
        Will generate random string of six-charter offline and store database
        KeyDatabase(shortUrl, status)
        Will have mem-cache/redis-cache that will always hold 100 unused keys to provide when request comes to application-server
        KGS also has to make sure not to give the same key to multiple servers. For that, it must synchronize (or get a lock on) 
        the data structure holding the keys before removing keys from it and giving them to a server

        Storage Capacity of KeyDatabase
            64^6 char => 68 billion unique url
            6 x 68 x 10^9 => 412 GB
```








