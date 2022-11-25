
Design : https://drive.google.com/file/d/1MU3KXgQ22K9LOzLnvpV0e17nziUwYCW9/view?usp=sharing
```
1. Functional Requirement
    - New updates to be part of search result in real time
    
2. Non-Functional Requirement
    - Low latency for read and search post
    - Slightly higher latency for write/create post
    - High availability
    - Scalability
    
3. Capacity Estimation
      Assumption
      -  500 million daily active user
      -  On averge 500 million tweet per day
      
      Storage Estimation:
        500 x 10^6 tweets/day * 500 Byte(size of each tweet)  => 250 x 10^6 => 250 GB per/day
      
      QPS: 
         -Read Query:
                    500 x 10^6
                    ----------- = 6000 request/sec
                    24 x 60 x 60
    
                   In peak time, it can serge to 2X of current request, So = 10,000 request/sec
    
         -Write Query
            -Assume 50 millions post are create each day = 600 requests/sec
     
4. Architecture deep-dive
    API:
        - searchPost(api_key, query, userId)
            searchResult = {
                   "query" : [postId-41, postId-90, postId-909,...., postId-89]
            }

    Database Schema:
        User(userId, name, phone, email, address, username, password, createdAt)
        Posts(postId, userId, text_photo_url, createdAt)

    Database Sharding:
        -userId(rejected due to hot box problem)
        -postId(considering)
    
    Component Design
        - Searching Index Servicee
        - User Service
        - Redis Cache
        - Application load balancer
        - MySql

    Searching Index service(This will save in in-memory datastore)
        -System will have Indexing-Service to helps to search the tweets faster
        -There are around 300K words in english and around 200 K for places and items etc.
            Total words = 300 K  + 200 K = 500 K words
        -Note : we are neglecting stopping words such as a, an, the, these etc.

    PostId generation format

        Timestamp1
        153513255_000001
        153513255_000002
        153513255_000003
    
        Timestamp2
        153513256_000001
        153513256_000002
        153513256_000003

    A. Index storage estimation
        Storage needed for searching-index = 500 K x 5 Bytes =  2500 KB = 2.5 MB

    B. PostId/tweetId storage estimation

        Calculation for 100 Years
        postId = (time_stamp) + _ + (post_uuid)
        bits required for timestamp = 86400 sec/day x 365 days x 100 Years = 3 x 2^30 = 30 bits
        timestamp required = 30 bit
        postId bits = 6000 posts/sec = 2^15 = 15 bits for postId

        total_bits = (timestamp = 30 bits) + (postId = 15 bits) = 45 bits requires for postId
        For safer side, postId = 64 bits looks good

    C. Search Index Storage
        In index, we are saving postId for period of two years
        50 x 10^6 posts per/day x 2 years x 365 Days = 3650 x 10^6 = 3.6 x 10^9 = 36 Billion tweets

        So, storage required for 36 billions post index = 36 x 10^9 x 8 Bytes = 300 GB

        Assume there are 50 important words on average in each posts
        = 50 x 300 = 15000 GB = 15 TB

    D. Sharding key for index-data on database
        -Words based sharding(Hot box problem)
        -postId based sharding(Considered) but aggregation layer required to show result to user

        #Ranking of result
        -First result will be sorted on bases of (likes, comments, share), then recency of tweets

    E.  -Save popular tweets on in-memory storage
            Cache : {
                "postId" : "Text"
            }

        -Save popular search result on in-memory storage
            Cache : {
                    "query" : [postId-145, postId-567]
            }
```