
Design: https://drive.google.com/file/d/1jywTj-BMFILeLoW1UEPWkMjf99QMbpms/view?usp=sharing
```
1. Functional requirement gathering
    	-Upload and view videos
	    -Analytics of videos(likes, views, comments, share)
	    -Search videos [usecase of trie]
	    -Add and view comment
	    -Like and dislike videos
	    -Resume video from where left -(Maintain user watchlist to implement this feature)
	    -Notification
	    -Recommendation videos
	    -Subscribe channels
	    -Adaptive streaming(View videos in different resolution)

2. Non-Functional requirement
        -High availability
        -Video uploaded should not be lost (Highly reliable)
        -Here, we prefer availability over consistency
        -Seamless buffering of videos


3. Estimation of scale(Include replication factor and autoscaling in mind while estimating)
    Assume, Daily active user on streaming-website 1 billions
    Each user see at most 5 videos daily

    Traffic estimation(Read QPS, Write QPS)
        -Read queries estimation(Video view estimation)
             5 x 10^9
            --------- = 5 x 10^4 = 50 K request/sec
             86400

        -Write queries estimation(Video upload estimation)
          Assume 1% of user upload videos
          So, 500 request/sec

    Storage estimation(Persistence storage)
        Assume average video size = 100 MB
        Storage required for one year
        86400 x 500 x 100 MB x 365 = 1.5 x 10^6 TB = 1500 PB


3. Trade Off
    A. CAP and PACELC
        -Write request : CP
        -Read request : AP

    B. Read and Write Latency
        -Upload and view will be separate service
        -Read query/View video should have low latency
        -Write query/Upload videos have high latency

4. Architecture deep-dive
    System API
        -CreateUser(userId, name, email, dob, phone, username, password)
        -getUser(userId)
        -UploadVideos(userId, videoId, title, description, tags = [], s3bucket_path, createdAt)
        -ViewVideo(userId, videoId, timestamp)
        -CreateComment(commentId, userId, videoId, createdAt)
        -LikeVideo(likeId, userId, videoId, timestamp)
        -videoMetaInfo(videoId, viewsCount, likesCount, shareCount)

    Database Schema
        -User(userId, name, email, dob, phone, username, password)
        -Videos(userId, videoId, title, description, size, tags = [], s3bucket_path, createdAt)
        -Comment(commentId, userId, videoID, text, createdAt)
        -ViewVideo(userId, videoId, timestamp)
        -LikesVideo(likeId, videoId, timestamp)
        -WatchList(deviceId, userId, videoId, chunks/timestamp)

    Database sharding mechanism(sharding-key)
        -userId(hot-bey problem)
        -videosId(hot-box problem)
        -Here, we consider sharding on basis on videoId,
         and to solve hot-box problem we use CDN and cache data at ISP also

    Caching mechanism
		-Global Cache and Write-around cache policy

    Component Design
        - Upload service
            - Segmentation
            - Encoding
            - Messaging Queue
        - View service
        - User service
        - CDN(S3 Object Store)
        - MySql
        - Redis Cache (Top trending videos)

###Upload Videos####
-Encoding(mp4, wav, etc) - Video can play on different devices
-Segmentation(m3u8 format) - Breaking videos into chunks of 6 sec, and each chunk in different resolution(480p, 720p, 1080p)
-Thumbnail upload or automatic generation
-Deduplication logic to ensure optimize storage
    -Deduplication should be done early in game to save server-computation resources
    -Create checksum value of videos and check for it in his database if something found it keep reference of it this this upload video
    -If new upload video have better quality, then older one then app will update video
-Message queue used to upload videos async
-Mysql database will store user-information, video-metadata, s3bucket-video-path
-CDN will store videos nearest location to user for reduce network latency

Adaptive streaming protocol
1. Mpeg DASH
2. HLS(Http live streaming)
                                  
```                 