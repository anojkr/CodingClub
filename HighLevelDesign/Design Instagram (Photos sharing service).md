
Design : https://drive.google.com/file/d/1wZPQhQaP57Vzrq6v16q1WCMLHZBw7fjr/view?usp=share_link
```
1. Functional Requirement
    - User should be able to upload/download/view photos
    - User can perform searches based on photos/videos titles  [X]
    - User can follow other user
    - System should generate and display user Newsfeed consisting of top photos
      from all the people the user follow
    - User can like, comment and tag on (Photos)

2. Non-functional requirement
    - System should be highly available
    - Read latency should be low
    - High reliable

3. Capacity Estimation

    Assumption
        -200 Kb size of each uploaded photos

    Storage Estimation
        - 500 Million daily active user
        - One Million user upload average two photos => 2 Millions photos uploaded every-day
            2 x 10^6 x 200 kb  => 400 GB  per/day
            400GB x 365  x 10 year => 1460 x 10^12 => 1460 TB

    Write QPS:
              2 x 10^6
            ------------------           => 23 photos/sec uploaded
             86.4 x 10^3 (SecondInDay)

            200 kb(photo size) x 23 -> 4.6 mbps

    Read QPS:
                500 x 10^6
            ------------------           => 6000 photos/sec
             86.4 x 10^3 (SecondInDay)

            200 kb(photo size) x 6 x 10^3 -> 1.2 gbps

3. Architectural deep-dive
    API :
        createPost(userId, text, image)
        uploadPhoto(userId, image)
        viewPhoto(photoId)
        getNewsfeeds(userId)
        getFollowers(userId)

    DataBase Schema :
        User(userId, name, email, password)
        Post(postId, userId, createdAt, text, s3_path)
        Photo(id, userId, createdAt, s3_path, lat, long, location)
        Tags(id, postId, tag_name, tag_id)
        Comment(id, postId, userId, createdAt, s3_path)
        Activity(EntityId, EntityType(Post, Comment, Page), count)
        NoOfLikes(entityId, count)
        FollowTable(userIdFollower, userIdFollowee)

    Component Design
        If we have single service to upload and view photo, Will face issue, Uploading photo is cpu-intensive and slow process,
        So system will not serve read request, as its busy with all write operation. Separating photos read and write requests
        will also allow us to scale and optimize each of these operations independently.
        Services
            -> Photo upload service
            -> Photo read service
            -> Post service (Create, Like, Comment)
            -> MysqlDB with Master-Salve and Two Replicas
            -> S3 Object Store
            -> Application Load Balancer
            -> API Gateway

        High Availability
            -> Have multiple replicas of database and object store

        Sharding
            userId -> Hot box problem(some user post/upload more photos than other users)
            postId/photoId-> but aggregator required to fetch all photos of user from all shards-instances


    ###TimeLine Generation#####

    First approach
        Steps
            1. Find all friends of userId
            2. For friendUserId in friends:
                    getPostOfUser(friendsUserId)
            3. Aggregate and return result rank-wise

    Second-Approach
        #Here we sacrifice write for better read
        Steps
            1. When user make a post
            2. Add this post to all his friends and followers time-line table

            The time-line table is present in-memory database as cache
            -Maximum 900 postId in in-memory datastore
            -Return result will be presented in paginated form to reduce loading time

    Celebrity user
        #Here celebrity user second-approach not work
            Each user have celebrity table that contains like of verified account userId
            celebrityId(userId-101, userId-290, userId-34, ....., userId-454)
            result = {getPostOfUser(userId-101), getPostOfUser(userId-290), getPostOfUser(userId-34)}

    So, Newsfeed will use hybrid approach
        1. For normal user use second-approach
        2. For celebrity user use On-load getPostOfUser(celebrityUserId)

    Ranking of top posts:
    Edge Ranking:
        - Affinity score : degree of relationship(direct, mutual friend etc)
        - Edge weight: comment have more weights than like
        - Time Decay:  Recent post  are more priority
```














